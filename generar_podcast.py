#!/usr/bin/env python3
"""Guion .md -> MP3 de podcast.

Uso:
    python generar_podcast.py guiones/01-ni-amaia-naiz.md          # un episodio
    python generar_podcast.py guiones/*.md                         # varios
    python generar_podcast.py guion.md --motor espeak              # prueba rapida (voz robotica)
    python generar_podcast.py guion.md --solo-medir                # solo cuenta pasos y estima duracion

Formato del guion (una instruccion por linea; lo demas se ignora):
    ES: texto           presentador en espanol
    EU: texto           frase en euskera
    [PAUSA n]           silencio de n segundos

Motores (--motor):
    piper     ES con Piper (es_ES-davefx-medium) + EU con phoonnx   [calidad buena, por defecto]
    espeak    ES y EU con espeak-ng                                   [robotico, sin descargas]

Requisitos: ffmpeg. Para `piper`: pip install piper-tts phoonnx  y  espeak-ng instalado en el sistema.
"""
import argparse, hashlib, re, shutil, subprocess, sys, wave
from pathlib import Path

# ---------------- Parametros ----------------
VOZ_ES = "es_ES-davefx-medium"                       # voz de Piper (se descarga con piper.download_voices)
VOZ_EU = "OpenVoiceOS/phoonnx_eu-ES_miro_espeak"     # alternativa: ..._dii_espeak
HUECO_ENTRE_FRASES = 0.6   # segundos de silencio entre dos pasos de voz seguidos
VELOCIDAD_EU = 1.15        # length_scale de phoonnx (>1 = mas lento; bueno para aprender)
VELOCIDAD_ES = 1.0
ESPEAK_VEL_ES = 150        # palabras/minuto en modo espeak
ESPEAK_VEL_EU = 120
BITRATE = "96k"
HZ = 24000
CARPETA_VOCES = Path("voces")
CARPETA_CACHE = Path(".cache_audio")
CARPETA_SALIDA = Path("podcasts")
# --------------------------------------------

RE_LINEA = re.compile(r"^\s*(ES|EU)\s*:\s*(.+?)\s*$")
RE_PAUSA = re.compile(r"^\s*\[PAUSA\s+([0-9]+(?:[.,][0-9]+)?)\s*\]\s*$", re.I)


def parsear(ruta):
    pasos = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        m = RE_LINEA.match(linea)
        if m:
            pasos.append(("voz", m.group(1), m.group(2)))
            continue
        m = RE_PAUSA.match(linea)
        if m:
            pasos.append(("pausa", None, float(m.group(1).replace(",", "."))))
    return pasos


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, **kw)
    if r.returncode != 0:
        sys.exit(f"Error ejecutando {' '.join(map(str, cmd))}\n{r.stderr.decode(errors='replace')[-800:]}")
    return r


# ---------------- Motores de voz ----------------
class Espeak:
    def __init__(self):
        if not shutil.which("espeak-ng"):
            sys.exit("Falta espeak-ng (apt install espeak-ng)")

    def sintetizar(self, idioma, texto, destino):
        v, s = ("es", ESPEAK_VEL_ES) if idioma == "ES" else ("eu", ESPEAK_VEL_EU)
        run(["espeak-ng", "-v", v, "-s", str(s), "-w", str(destino), texto])


class PiperPhoonnx:
    def __init__(self):
        self.es_modelo = CARPETA_VOCES / f"{VOZ_ES}.onnx"
        if not self.es_modelo.exists():
            CARPETA_VOCES.mkdir(exist_ok=True)
            print(f"Descargando voz {VOZ_ES} ...")
            run([sys.executable, "-m", "piper.download_voices", VOZ_ES, "--download-dir", str(CARPETA_VOCES)])
        self._eu = None

    def _voz_eu(self):
        if self._eu is None:
            try:
                from phoonnx.model_manager import TTSModelManager
            except ImportError:
                sys.exit("Falta phoonnx: pip install phoonnx")
            mgr = TTSModelManager()
            mgr.load()
            if VOZ_EU not in mgr.voices:
                print("Actualizando lista de voces de phoonnx ...")
                try:
                    mgr.get_ovos_voice_list()
                except Exception as e:  # noqa
                    sys.exit(f"No se pudo obtener la lista de voces: {e}")
                if VOZ_EU not in mgr.voices:
                    eu = [v for v in mgr.voices if "eu-ES" in v]
                    sys.exit(f"Voz {VOZ_EU} no encontrada. Voces de euskera disponibles: {eu}")
            self._eu = mgr.voices[VOZ_EU].load()
        return self._eu

    def sintetizar(self, idioma, texto, destino):
        if idioma == "ES":
            run(["piper", "-m", str(self.es_modelo), "-f", str(destino), "--length-scale", str(VELOCIDAD_ES)]
                if shutil.which("piper") else
                [sys.executable, "-m", "piper", "-m", str(self.es_modelo), "-f", str(destino),
                 "--length-scale", str(VELOCIDAD_ES)], input=texto.encode("utf-8"))
        else:
            from phoonnx.voice import SynthesisConfig  # type: ignore
            voz = self._voz_eu()
            cfg = SynthesisConfig(length_scale=VELOCIDAD_EU)
            with wave.open(str(destino), "wb") as w:
                voz.synthesize_wav(texto, w, syn_config=cfg)


def crear_motor(nombre):
    return Espeak() if nombre == "espeak" else PiperPhoonnx()


# ---------------- Audio ----------------
def duracion_wav(ruta):
    with wave.open(str(ruta), "rb") as w:
        return w.getnframes() / w.getframerate()


def normalizar(origen, destino):
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(origen), "-ar", str(HZ), "-ac", "1",
         "-c:a", "pcm_s16le", str(destino)])


def silencio(seg, destino):
    if not destino.exists():
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"anullsrc=r={HZ}:cl=mono",
             "-t", f"{seg:.3f}", "-c:a", "pcm_s16le", str(destino)])
    return destino


def trozo_voz(motor, nombre_motor, idioma, texto):
    """WAV normalizado de una frase; cacheado por (motor, idioma, texto, velocidad)."""
    CARPETA_CACHE.mkdir(exist_ok=True)
    clave = f"{nombre_motor}|{idioma}|{texto}|{VELOCIDAD_EU}|{VELOCIDAD_ES}|{VOZ_ES}|{VOZ_EU}"
    h = hashlib.sha1(clave.encode()).hexdigest()[:16]
    final = CARPETA_CACHE / f"{h}.wav"
    if not final.exists():
        crudo = CARPETA_CACHE / f"{h}.raw.wav"
        motor.sintetizar(idioma, texto, crudo)
        normalizar(crudo, final)
        crudo.unlink()
    return final


def generar(guion, nombre_motor, solo_medir):
    pasos = parsear(guion)
    n_voz = sum(1 for p in pasos if p[0] == "voz")
    pausas = sum(p[2] for p in pasos if p[0] == "pausa")
    print(f"{guion}: {len(pasos)} pasos ({n_voz} de voz, {sum(1 for p in pasos if p[0]=='pausa')} pausas, {pausas:.0f} s de pausas)")
    if solo_medir or not pasos:
        return
    motor = crear_motor(nombre_motor)
    lista, total, previo_voz = [], 0.0, False
    for i, (tipo, idioma, valor) in enumerate(pasos, 1):
        if tipo == "voz":
            if previo_voz:
                lista.append(silencio(HUECO_ENTRE_FRASES, CARPETA_CACHE / f"sil_{HUECO_ENTRE_FRASES}.wav"))
                total += HUECO_ENTRE_FRASES
            w = trozo_voz(motor, nombre_motor, idioma, valor)
            lista.append(w)
            total += duracion_wav(w)
            previo_voz = True
            print(f"  [{i}/{len(pasos)}] {idioma}: {valor[:60]}", flush=True)
        else:
            lista.append(silencio(valor, CARPETA_CACHE / f"sil_{valor}.wav"))
            total += valor
            previo_voz = False
    CARPETA_SALIDA.mkdir(exist_ok=True)
    txt = CARPETA_CACHE / "lista.txt"
    txt.write_text("".join(f"file '{p.resolve()}'\n" for p in lista), encoding="utf-8")
    salida = CARPETA_SALIDA / (Path(guion).stem.split("-")[0] + ".mp3")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(txt),
         "-c:a", "libmp3lame", "-b:a", BITRATE, "-ar", str(HZ), "-ac", "1", str(salida)])
    print(f"-> {salida}  duracion {int(total//60)}:{int(total%60):02d}  ({salida.stat().st_size/1e6:.1f} MB)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("guiones", nargs="+")
    ap.add_argument("--motor", choices=["piper", "espeak"], default="piper")
    ap.add_argument("--solo-medir", action="store_true")
    ap.add_argument("--bitrate", default=None, help="p. ej. 48k (por defecto 96k)")
    a = ap.parse_args()
    if a.bitrate:
        global BITRATE
        BITRATE = a.bitrate
    if not shutil.which("ffmpeg") and not a.solo_medir:
        sys.exit("Falta ffmpeg")
    for g in a.guiones:
        generar(g, a.motor, a.solo_medir)


if __name__ == "__main__":
    main()
