# Proyecto: Podcast de euskera para el aitona

## Objetivo
App para que mi aitona (abuelo) aprenda euskera **escuchando podcasts mientras pasea**, al estilo de *Euskara Satorra* (Beñat Erezuma), que le gusta.

- Cada lección = **un episodio de audio de ~10 minutos**.
- El audio se **genera con IA** (TTS). No quiero grabar nada yo.
- La progresión de temas debe seguir el curso gratuito de Hiru: https://www.hiru.eus/es/e-ikasi/idiomas/ikasten (lista real de 24 unidades en `docs/unidades-hiru.md`).

## Restricciones
- **Coste cero**: nada de pago, ni hosting ni APIs.
- El aitona tiene **iPhone** → la app será una **web (PWA)** que se añade a la pantalla de inicio desde Safari.
- Usuario: él, persona mayor → letra grande, botones grandes, muy simple.
- TTS **open source / local** (en mi PC con Windows + WSL, o en Docker).
- No copiar contenido de Euskara Satorra ni de Hiru; solo enlazar. Los guiones son propios.

## Estado actual

```
euskera/
├── PROYECTO.md            ← este archivo
├── index.html             ← primera versión de la web (lecciones con texto + Web Speech). A rehacer como reproductor de podcast
├── guiones/
│   └── 01-saludos.md      ← guion del episodio 1 (hecho)
├── generar_podcast.py     ← guion .md → MP3 (sin probar con voces reales)
├── Dockerfile             ← imagen con ffmpeg + Piper + phoonnx y voces precargadas (sin probar)
├── INSTALAR.md            ← instalación en WSL
└── DOCKER.md              ← uso con Docker
```

### Formato de los guiones (`guiones/NN-tema.md`)
Una instrucción por línea; el resto se ignora:
- `ES: texto` → presentador en español
- `EU: texto` → frase en euskera
- `[PAUSA n]` → silencio de n segundos (para que repita en voz alta)

Estructura de cada episodio: bienvenida → frases nuevas (oír, explicar, repetir con pausa) → mini diálogo → repaso "yo digo en español, tú en euskera" → despedida y avance del siguiente episodio.

### Generación de audio (`generar_podcast.py`)
- Español: **Piper**, voz `es_ES-davefx-medium` (`piper -m modelo.onnx -f salida.wav`, texto por stdin).
- Euskera: **phoonnx**, voz `OpenVoiceOS/phoonnx_eu-ES_miro_espeak` (alternativa `..._dii_espeak`). Licencia CC BY-NC-ND (uso no comercial OK).
- ffmpeg normaliza cada trozo a 24 kHz mono, añade silencios (`anullsrc`), concatena y exporta MP3 96 kbps a `podcasts/`.
- Parámetros arriba del script: `VOZ_ES`, `VOZ_EU`, `HUECO_ENTRE_FRASES`, `VELOCIDAD_EU` (length_scale, >1 = más lento).
- Comprobado solo el parser: el episodio 1 son 153 pasos (68 ES, 44 EU, 41 pausas, 128 s de pausas). **La síntesis no se ha ejecutado nunca.**

Alternativas si algo falla: AhoTTS (UPV/EHU, euskera + castellano, más robótico); edge-tts (voces Microsoft `eu-ES-AinhoaNeural`/`AnderNeural`, necesita internet, no oficial).

## Próximos pasos
1. **Probar la generación** del episodio 1 (Docker o WSL) y arreglar errores. Verificar la API real de phoonnx y el comando de descarga de voces de Piper.
2. Medir duración; ajustar guion o `VELOCIDAD_EU` para llegar a ~10 min.
3. ~~Conseguir la lista de unidades de Hiru~~ → hecho: `docs/unidades-hiru.md` (24 episodios, un episodio por unidad).
4. Escribir el resto de guiones (mismo formato y estructura).
5. ~~Rehacer `index.html` como reproductor de podcast~~ → hecho (`index.html`, `sw.js`, `manifest.json`, `icons/`, `episodios.json`). Falta probarlo en un iPhone real. Para publicar un episodio: poner el MP3 en `podcasts/NN.mp3` y `"disponible": true` en `episodios.json`. Requisitos originales:
   - Lista de episodios + botón grande "▶ Continuar" (siguiente episodio no terminado).
   - Recordar episodio y segundo donde se quedó (localStorage).
   - **Media Session API** para controles en la pantalla de bloqueo (play/pausa/±15 s/siguiente) — clave para pasear con el móvil en el bolsillo.
   - `manifest.json` + icono para "Añadir a pantalla de inicio" en iOS.
   - Service worker para cachear los MP3 y escuchar sin datos (ojo: iOS puede borrar la caché si no se usa).
6. Publicar gratis en **GitHub Pages** (web + MP3) y probar en un iPhone real con la pantalla bloqueada.
7. Que alguien que hable euskera revise los guiones.

## Notas
- Probar en iPhone que el audio sigue sonando con la pantalla bloqueada y que los controles aparecen.
- Mantener los MP3 ligeros (96 kbps mono ≈ 7 MB por episodio de 10 min) por el límite de GitHub Pages.
