#!/usr/bin/env python3
"""Guarda en local el TEXTO de las 24 lecciones de Hiru (tu cuenta de ikasten.siacco.com).

Solo para usarlo como referencia al escribir guiones PROPIOS. La carpeta hiru_texto/ esta en .gitignore:
no se sube ni se publica.

    pip install playwright && playwright install chromium
    python scrape_hiru.py            # se abre un navegador: inicia sesion en el (espera hasta 10 min)
    python scrape_hiru.py 1 2 3      # solo esas lecciones (numero de episodio)
"""
import json, re, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

LECCIONES = json.loads(Path("docs/lecciones-hiru-urls.json").read_text(encoding="utf-8"))
SALIDA = Path("hiru_texto")


def texto_pagina(page):
    partes = []
    for fr in page.frames:
        try:
            partes.append(fr.inner_text("body", timeout=3000))
        except Exception:
            pass
    return "\n".join(p for p in partes if p.strip())


def abrir(page, url):
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(1500)


def main():
    quiero = {int(a) for a in sys.argv[1:]}
    with sync_playwright() as p:
        nav = p.chromium.launch(headless=False)
        page = nav.new_context().new_page()
        page.goto("https://ikasten.siacco.com/a/home")
        print("Se ha abierto un navegador: inicia sesion en ikasten (tienes 10 minutos)...", flush=True)
        page.wait_for_url(lambda u: "/a/" in u and "logged-out" not in u, timeout=600_000)
        page.wait_for_timeout(3000)
        print("Sesion iniciada. Leyendo lecciones...", flush=True)
        for lec in LECCIONES:
            n = lec["ep"]
            if quiero and n not in quiero:
                continue
            d = SALIDA / f"{n:02d}"
            d.mkdir(parents=True, exist_ok=True)
            abrir(page, lec["url"])
            (d / "00-leccion.txt").write_text(texto_pagina(page), encoding="utf-8")
            enlaces = page.eval_on_selector_all(
                'a[href*="/activity/"]', "els => [...new Set(els.map(e => e.href))]")
            print(f"[{n:02d}] {lec['titulo_pagina']}: {len(enlaces)} actividades")
            for i, url in enumerate(enlaces, 1):
                try:
                    abrir(page, url)
                    (d / f"{i:02d}-{url.rsplit('/', 1)[-1]}.txt").write_text(
                        f"{url}\n\n{texto_pagina(page)}", encoding="utf-8")
                except Exception as e:  # noqa
                    print("   fallo", url, e)
        nav.close()
    print("Listo. Comprime la carpeta hiru_texto/ y pasamela.")


if __name__ == "__main__":
    main()
