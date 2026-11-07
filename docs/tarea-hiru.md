# Tarea: leer las lecciones de Hiru y reescribir los guiones

Se hace en una sesión de Claude Code en el ordenador del propietario (Remote Control), porque Hiru/ikasten bloquean el acceso desde servidores en la nube.

## Reglas
- El propietario inicia sesión **a mano** en el navegador que se abra. No pedir ni guardar la contraseña.
- El texto de Hiru es **solo referencia**: se queda en `hiru_texto/` (en `.gitignore`). Nunca subirlo ni copiarlo literal. Los guiones son propios (frases y explicaciones nuevas) siguiendo los temas, vocabulario y estructuras de cada lección.
- No saltarse protecciones del sitio (nada de disfrazar el navegador ni reintentos masivos). Si algo falla, parar y contarlo.

## Pasos
1. `pip install playwright` y `python -m playwright install chromium`.
2. Probar con 2 lecciones: `python scrape_hiru.py 1 2`. Se abre un navegador VISIBLE: avisar al propietario para que inicie sesión (el script espera hasta 10 min y sigue solo). Guarda el texto en `hiru_texto/NN/`. URLs en `docs/lecciones-hiru-urls.json`.
3. Revisar lo leído. Si trae vocabulario (Hiztegia), explicaciones (Jakin) y ejercicios (Egin), lanzar las 24: `python scrape_hiru.py`. Si sale vacío o solo menús, ajustar selectores en `scrape_hiru.py` (iframes, pestañas que se cargan al pulsar) y probar con 1 lección.
4. Actualizar los datos de cada episodio en `herramientas/crear_guiones.py` (diccionario `EPISODIOS`: `items` (euskera, español, nota), `dialogo`, `siguiente`), manteniendo la estructura: bienvenida → frases nuevas → mini diálogo → repaso "yo digo en español, tú en euskera" → despedida. El 01 está a mano en `guiones/01-ni-amaia-naiz.md`: ajustarlo si la lección 1 lo pide. Los repasos (4, 8, 12, 16, 20, 24) salen solos de los 3 anteriores.
5. Regenerar: `python herramientas/crear_guiones.py` y `python herramientas/crear_ejercicios.py`. Medir: `python generar_podcast.py guiones/*.md --solo-medir` (objetivo ~10 min por episodio).
6. `git status` (comprobar que `hiru_texto/` NO aparece) y commit + push solo de `herramientas/crear_guiones.py`, `guiones/`, `ejercicios.json` (y `scrape_hiru.py` si cambió), a la rama `ccr-4af4a132-aapwbb`.
7. Resumir al propietario qué cambió por episodio. Para regenerar el audio: GitHub → Actions → "Generar audio" → modo `episodios`, motor `styletts`, preguntas `subida` (voz Antton).
