#!/usr/bin/env python3
"""Entra en ikasten.siacco.com con IKASTEN_USER / IKASTEN_PASS (variables de entorno) y guarda el TEXTO
de las lecciones indicadas en salida_ikasten/. Solo para referencia personal al escribir guiones propios:
esa carpeta NO se sube al repositorio (queda como artefacto temporal del workflow).

    python herramientas/scrape_ikasten.py 1 2        # episodios 1 y 2
    python herramientas/scrape_ikasten.py            # los 24
"""
import json, os, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

USER, PASS = os.environ.get("IKASTEN_USER", ""), os.environ.get("IKASTEN_PASS", "")
LECCIONES = json.loads(Path("docs/lecciones-hiru-urls.json").read_text(encoding="utf-8"))
SALIDA = Path("salida_ikasten")
HOME = "https://ikasten.siacco.com/a/home"
quiero = {int(a) for a in sys.argv[1:] if a.isdigit()}


def estructura(page, titulo):
    """Imprime la estructura de la pagina SIN valores (para depurar el login sin exponer datos)."""
    print(f"--- {titulo}: url={page.url!r} titulo={page.title()!r}")
    for el in page.query_selector_all("input, button, a[href*='login'], a[href*='sign'], form"):
        try:
            tag = el.evaluate("e => e.tagName.toLowerCase()")
            attrs = {a: el.get_attribute(a) for a in ("type", "name", "id", "placeholder", "autocomplete", "action", "href") if el.get_attribute(a)}
            txt = (el.inner_text() or "").strip()[:40] if tag in ("button", "a") else ""
            print("   ", tag, attrs, repr(txt), "visible" if el.is_visible() else "oculto")
        except Exception:
            pass


def hay_password(page):
    return any(e.is_visible() for e in page.query_selector_all("input[type=password]"))


def login(page):
    page.on("response", lambda r: print("   [red]", r.request.method, r.status, r.url.split("?")[0][:110])
            if r.request.method in ("POST", "PUT") or "login" in r.url or "session" in r.url or "token" in r.url else None)
    page.goto(HOME, wait_until="networkidle")
    page.wait_for_timeout(1500)
    for paso in range(3):
        if not hay_password(page) and paso > 0:
            break
        campos = [e for e in page.query_selector_all("input") if e.is_visible()
                  and (e.get_attribute("type") or "text") in ("text", "email")]
        if campos:
            campos[0].click(); campos[0].fill(""); campos[0].type(USER, delay=25)
        if hay_password(page):
            page.click("input[type=password]"); page.fill("input[type=password]", ""); page.type("input[type=password]", PASS, delay=25)
        print(f"   paso {paso}: usuario con {len(USER)} caracteres, clave con {len(PASS)} caracteres")
        boton = None
        for sel in ("button[type=submit]", "input[type=submit]", "button:has-text('Sartu')", "button:has-text('Entrar')",
                    "button:has-text('Acceder')", "button:has-text('Iniciar')", "button:has-text('Login')", "button"):
            b = page.query_selector(sel)
            if b and b.is_visible():
                boton = b
                break
        if boton:
            boton.click()
        else:
            page.keyboard.press("Enter")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3500)
        print("   tras pulsar: url =", page.url)
        try:
            print("   texto de la pagina:", re.sub(r"\s+", " ", page.inner_text("body"))[:300])
        except Exception:
            pass
        if "/a/" in page.url and "logged-out" not in page.url and not hay_password(page):
            return True
    return "/a/" in page.url and "logged-out" not in page.url and not hay_password(page)


def texto(page):
    partes = []
    for fr in page.frames:
        try:
            partes.append(fr.inner_text("body", timeout=4000))
        except Exception:
            pass
    return "\n".join(p for p in partes if p.strip())


def abrir(page, url):
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(1200)


def main():
    if not USER or not PASS:
        sys.exit("Faltan los secretos IKASTEN_USER / IKASTEN_PASS")
    SALIDA.mkdir(exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        page = nav.new_context(locale="es-ES", viewport={"width": 1280, "height": 900}).new_page()
        page.goto(HOME, wait_until="networkidle")
        page.wait_for_timeout(1500)
        estructura(page, "antes de entrar")
        if not login(page):
            estructura(page, "login FALLIDO")
            page.screenshot(path=str(SALIDA / "login-fallido.png"))
            nav.close()
            sys.exit("No se pudo iniciar sesion (revisa la estructura impresa arriba)")
        print("Sesion iniciada. URL:", page.url)
        for lec in LECCIONES:
            n = lec["ep"]
            if quiero and n not in quiero:
                continue
            d = SALIDA / f"{n:02d}"
            d.mkdir(parents=True, exist_ok=True)
            abrir(page, lec["url"])
            (d / "00-leccion.txt").write_text(texto(page), encoding="utf-8")
            enlaces = page.eval_on_selector_all('a[href*="/activity/"]', "els => [...new Set(els.map(e => e.href))]")
            print(f"[{n:02d}] {lec['titulo_pagina']}: {len(enlaces)} actividades")
            for i, url in enumerate(enlaces, 1):
                try:
                    abrir(page, url)
                    (d / f"{i:02d}-{url.rsplit('/', 1)[-1]}.txt").write_text(f"{url}\n\n{texto(page)}", encoding="utf-8")
                except Exception as e:  # noqa
                    print("   fallo", url, str(e)[:100])
        nav.close()
    print("Listo.")


if __name__ == "__main__":
    main()
