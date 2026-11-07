#!/usr/bin/env python3
"""Genera una muestra de euskera con StyleTTS2-eu (HiTZ/UPV-EHU, Apache-2.0).

Se ejecuta DENTRO del repositorio clonado AArriandiaga/StyleTTS2_basque (para que encuentre sus modulos):
    cd StyleTTS2_basque && python ../herramientas/styletts_muestra.py ../muestras
Necesita en el repo clonado: Models/..., Utils/... (ver .github/workflows/styletts.yml) y los WAV de referencia en refs/.
"""
import sys, time
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path.cwd()))
from inference import Synthesizer  # noqa: E402

SALIDA = Path(sys.argv[1] if len(sys.argv) > 1 else "../muestras")
SALIDA.mkdir(parents=True, exist_ok=True)
CFG = "Models/Basque_Multispeaker_Phoneme_wavlm_normal/config_basque_multispeaker_phoneme_wavlm_800_2nd_normal.yml"
CKPT = "Models/Basque_Multispeaker_Phoneme_wavlm_normal/epoch_2nd_00030.pth"
FRASES = [
    "Kaixo! Ni Amaia naiz. Zu Mikel zara.",
    "Nor zara zu? Ni Xabi naiz, Zarauzkoa naiz.",
    "Zer moduz zaude? Ondo nago, eskerrik asko.",
    "Amaia amonarengana joan da. Bai auto garestia!",
]

t0 = time.time()
synth = Synthesizer(config=CFG, checkpoint=CKPT, ref="refs/antton.wav", device="cpu")
print(f"modelo cargado en {time.time()-t0:.0f}s", flush=True)
for voz in ("antton", "maider"):
    ref = f"refs/{voz}.wav"
    trozos, pausa = [], np.zeros(int(24000 * 0.6), dtype=np.float32)
    for f in FRASES:
        t1 = time.time()
        wav = synth.run(f, ref=ref)
        print(f"[{voz}] {f!r}: {len(wav)/24000:.1f}s de audio en {time.time()-t1:.0f}s", flush=True)
        trozos += [wav.astype(np.float32), pausa]
    out = SALIDA / f"styletts-{voz}.wav"
    sf.write(out, np.concatenate(trozos), 24000)
    print("guardado", out, flush=True)
