#!/usr/bin/env python3
"""Muestra de PREGUNTAS con StyleTTS2-eu (voz Antton) en tres versiones, para comparar la entonación:
  normal     -> parámetros por defecto
  expresiva  -> más peso del texto en la prosodia (beta y embedding_scale más altos)
  subida     -> normal + subida gradual del tono al final de la pregunta (Praat / parselmouth)
Se ejecuta dentro del repo clonado StyleTTS2_basque:  python ../herramientas/styletts_preguntas.py ../muestras
"""
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path.cwd()))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from inference import Synthesizer  # noqa: E402
from entonacion import subir_final  # noqa: E402

SALIDA = Path(sys.argv[1] if len(sys.argv) > 1 else "../muestras")
SALIDA.mkdir(parents=True, exist_ok=True)
CFG = "Models/Basque_Multispeaker_Phoneme_wavlm_normal/config_basque_multispeaker_phoneme_wavlm_800_2nd_normal.yml"
CKPT = "Models/Basque_Multispeaker_Phoneme_wavlm_normal/epoch_2nd_00030.pth"
FRASES = ["Zer moduz zaude?", "Zu Mikel zara?", "Auto hau berria da?", "Nor zara zu?", "Nongoa zara?", "Zuk liburu bat daukazu?"]
SR = 24000

synth = Synthesizer(config=CFG, checkpoint=CKPT, ref="refs/antton.wav", device="cpu")
pausa = np.zeros(int(SR * 0.8), dtype=np.float32)
versiones = {"normal": [], "expresiva": [], "subida": []}
for f in FRASES:
    w = synth.run(f).astype(np.float32)
    versiones["normal"] += [w, pausa]
    versiones["subida"] += [subir_final(w, SR, f), pausa]
    e = synth.run(f, beta=0.95, embedding_scale=2.0).astype(np.float32)
    versiones["expresiva"] += [e, pausa]
    print("ok", f, flush=True)
for nombre, trozos in versiones.items():
    out = SALIDA / f"pregunta-antton-{nombre}.wav"
    sf.write(out, np.concatenate(trozos), SR)
    print("guardado", out, flush=True)
