# Generar los episodios (WSL / Linux)

```bash
sudo apt install ffmpeg espeak-ng python3-venv
python3 -m venv .venv && source .venv/bin/activate
pip install piper-tts phoonnx
```

Probar sin descargar voces (robótico, solo para comprobar que todo encaja):
```bash
python generar_podcast.py guiones/01-ni-amaia-naiz.md --motor espeak
```

Con voces buenas (Piper para español, phoonnx para euskera; las voces se descargan de Hugging Face la primera vez):
```bash
python generar_podcast.py guiones/01-ni-amaia-naiz.md
```
El MP3 sale en `podcasts/01.mp3`. Después, en `episodios.json` pon `"disponible": true` para ese episodio.

`--solo-medir` cuenta pasos y pausas sin generar audio. Parámetros (voces, velocidad, hueco entre frases) arriba de `generar_podcast.py`.

Estado: la ruta `--motor espeak` está probada de principio a fin. La ruta de Piper + phoonnx sigue sin probarse con voces reales (la descarga de voces estaba bloqueada en el entorno donde se escribió). Los nombres exactos de la voz de euskera pueden necesitar ajuste; si no la encuentra, el script lista las voces `eu-ES` disponibles.
