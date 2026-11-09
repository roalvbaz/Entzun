#!/usr/bin/env python3
"""Anade A2, B1 y B2 a episodios.json. Un episodio queda disponible cuando existe su MP3 en podcasts/.

Se puede repetir: por ejemplo, despues de generar el audio.
    python herramientas/crear_episodios.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crear_guiones import EPISODIOS  # noqa: E402
from temas_hiru import NIVELES  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
ROMANOS = ["I", "II", "III", "IV", "V", "VI"]
INFO = {
    "A2": ("Nivel A2", "Pasado, futuro y hablar de lo cotidiano", "#2d46b9"),
    "B1": ("Nivel B1", "Frases más largas y matices", "#8d67ab"),
    "B2": ("Nivel B2", "Lo imaginario, opiniones y expresiones", "#e8742a"),
}


def main():
    ruta = RAIZ / "episodios.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    niveles = [n for n in datos["niveles"] if n["id"] == "A1"]
    for nombre, de, a in NIVELES[1:]:
        lista, bloque = [], 0
        for n in range(de, a + 1):
            ep = EPISODIOS[n]
            repaso = ep.get("repaso")
            audio = f"podcasts/{n:02d}.mp3"
            lista.append({"id": n, "titulo": f"Repaso {ROMANOS[bloque]}" if repaso else ep["titulo"], "bloque": ROMANOS[bloque],
                          "audio": audio, "disponible": (RAIZ / audio).exists()})
            bloque += 1 if repaso else 0
        titulo, descripcion, color = INFO[nombre]
        niveles.append({"id": nombre, "nombre": titulo, "descripcion": descripcion, "color": color, "episodios": lista})
    datos["niveles"] = niveles
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    print({n["id"]: sum(e["disponible"] for e in n["episodios"]) for n in niveles})


if __name__ == "__main__":
    main()
