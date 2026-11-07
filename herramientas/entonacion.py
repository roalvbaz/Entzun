"""Subida de entonación al final de las preguntas (para voces TTS que las dicen planas).
Usa Praat a través de parselmouth: PSOLA, sin cambiar la duración."""
import re

import numpy as np

PARTICULAS = ("nor", "non", "nola", "zer", "zein", "zenbat", "noiz", "zergatik", "nora", "nondik",
              "nongo", "nolako", "noren", "norena", "norekin", "norentzat", "nori", "nork")


def es_pregunta_si_no(texto):
    """True si la pregunta no empieza por partícula interrogativa (sí/no: entonación más ascendente)."""
    ultima = re.split(r"[.!]\s+", texto.strip())[-1]
    palabras = re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]+", ultima.lower())
    return bool(palabras) and not palabras[0].startswith(PARTICULAS)


def subir_final(wav, sr, texto, subida_si_no=1.45, subida_parcial=1.15, tramo=0.55):
    """Si el texto termina en '?', sube gradualmente el tono en los últimos `tramo` segundos con voz."""
    if not texto.strip().endswith("?"):
        return wav
    import parselmouth
    from parselmouth.praat import call
    snd = parselmouth.Sound(wav.astype(np.float64), sampling_frequency=sr)
    pitch = snd.to_pitch(time_step=0.01, pitch_floor=60, pitch_ceiling=400)
    f0 = pitch.selected_array["frequency"]
    t = pitch.xs()
    voz = t[f0 > 0]
    if len(voz) < 5:
        return wav
    fin = float(voz[-1])
    ini = max(float(voz[0]), fin - tramo)
    factor = subida_si_no if es_pregunta_si_no(texto) else subida_parcial
    manip = call(snd, "To Manipulation", 0.01, 60, 400)
    tier = call(manip, "Extract pitch tier")
    pasos = 6
    for i in range(pasos):                      # rampa: cada tramo un poco más alto
        a = ini + (fin - ini) * i / pasos
        b = ini + (fin - ini) * (i + 1) / pasos
        f = 1 + (factor - 1) * (i + 1) / pasos
        call(tier, "Multiply frequencies", a, b if i < pasos - 1 else snd.duration, f)
    call([tier, manip], "Replace pitch tier")
    out = call(manip, "Get resynthesis (overlap-add)")
    y = out.values[0].astype(np.float32)
    return y[: len(wav)] if len(y) >= len(wav) else np.pad(y, (0, len(wav) - len(y)))
