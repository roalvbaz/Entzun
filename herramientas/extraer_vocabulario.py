#!/usr/bin/env python3
"""Saca de la copia local (curso/) las palabras sueltas de cada leccion a herramientas/vocabulario.json.

Solo palabras y expresiones cortas, sin frases. Cada palabra se queda en la primera leccion donde aparece.
    python herramientas/extraer_vocabulario.py
"""
import html, json, re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
API = RAIZ / "curso" / "api"
MAX_EU, MAX_ES = 3, 5
SIN_PALABRA = re.compile(r"[0-9=:;_«»\"]")
INSTRUCCION = ("Irakurri ", "Entzun ", "Lotu ", "Hona ", "Honako ", "Honek ", "Ikasi ", "Lee ", "Escucha ", "Une ")
NUMEROS = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce",
           "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte"]


def texto(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def limpia_es(s):
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\b(el|la|los|las)/(el|la|los|las)\b", r"\1", s)
    s = re.sub(r"(\w)/\w+", r"\1", s)  # profesor/a -> profesor
    return s.strip(" ,.;:¡!¿?")


def limpia_eu(s):
    return s.split("/")[0].strip(" ,.;:")


def valida(eu, es):
    if not eu or not es or SIN_PALABRA.search(eu) or SIN_PALABRA.search(es):
        return False
    if len(eu.split()) > MAX_EU or len(es.split()) > MAX_ES or eu.endswith(("?", "!")) or eu.isupper():
        return False
    if len(es) > 32 or not es[0].isalpha():
        return False
    if (" " in eu and eu[0].isupper()) or re.match(r"[a-z]\)", eu) or "edo " in es:  # titulos y apartados, no palabras
        return False
    if eu.startswith(INSTRUCCION) or es.startswith(INSTRUCCION):
        return False
    return eu.lower() != es.lower()


def pares(a):
    """(euskera, espanol) de una actividad, segun como la haya maquetado el curso."""
    ct = a["attributes"]["content"] or ""
    if a["attributes"]["category"] == "flashcards":
        for es, eu in re.findall(r"<li>([^=<]+)=([^<]+)</li>", ct):
            yield eu, es
        return
    if 'class="linker"' in ct and "hiztegi" in (a["attributes"]["title"] or "").lower():
        for eu, es in re.findall(r"<li>([^=<]+)=([^<]+)</li>", ct):
            yield eu, es
        return
    if "hiztegi" not in (a["attributes"]["title"] or "").lower() and "hiztegi" not in ct[:300].lower():
        return
    for eu, es in re.findall(r"<strong>([^<:]+?)(?::\s*</strong>|</strong>\s*:)\s*([^<]+)<", ct):
        yield eu, es
    for eu, es in re.findall(r"<strong>\s*\d+\.?\s*</strong>\s*([^<(]+?)\s*\(([^)<]+)\)", ct):  # 1. Urtarril (Enero)
        yield eu, es
    for eu, es in re.findall(r"<strong>([^<:]+)</strong>\s*(?:<em>|<i>)?\s*\(([^)<]+)\)", ct):  # ikusmen (vista)
        yield eu, es
    for num, eu in re.findall(r"<p>\s*(\d+)\s*:\s*<strong>([^<]+)</strong>", ct):
        if int(num) < len(NUMEROS):
            yield eu, NUMEROS[int(num)]
    for es, eu in re.findall(r"<p>\s*\(([^)<]+)\)\s*<strong>([^<]+)</strong>", ct):
        yield eu, es
    for eu, es in re.findall(r"<p>\s*([^<(]+?)\s*<em>\s*\(([^)<]+)\)\s*</em>\s*</p>", ct):
        yield eu, es
    for fila in re.findall(r"<tr[^>]*>(.*?)</tr>", ct, flags=re.S):
        celdas = [texto(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", fila, flags=re.S)]
        if len(celdas) == 2:
            yield celdas[0], celdas[1]


def main():
    curso = json.loads((API / "courses" / "HK1.json").read_text(encoding="utf-8"))
    vistas, salida = set(), {}
    for n, l in enumerate(curso["data"]["relationships"]["lessons"]["data"], 1):
        leccion = json.loads((API / "lessons" / f"{l['id']}.json").read_text(encoding="utf-8"))
        lista = []
        for a in leccion["included"]:
            if a["type"] != "activity":
                continue
            for eu, es in pares(a):
                eu, es = limpia_eu(texto(eu)), limpia_es(texto(es))
                if valida(eu, es) and eu.lower() not in vistas:
                    vistas.add(eu.lower())
                    lista.append([eu, es])
        if lista:
            salida[str(n)] = lista
    destino = Path(__file__).with_name("vocabulario.json")
    destino.write_text(json.dumps(salida, ensure_ascii=False, indent=0), encoding="utf-8")
    print(len(salida), "lecciones,", sum(map(len, salida.values())), "palabras")


if __name__ == "__main__":
    main()
