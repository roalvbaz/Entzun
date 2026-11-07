#!/usr/bin/env python3
"""Genera ejercicios.json (tests y rellenar huecos) a partir de las frases de crear_guiones.py.

    python herramientas/crear_ejercicios.py
Formato: {"A1": {"<episodio>": [pregunta, ...]}}
  pregunta = {"t": "test"|"hueco", "p": enunciado, "s": pista (opcional), "o": [opciones], "c": indice correcto}
"""
import json, random, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crear_guiones import EPISODIOS  # noqa: E402

PALABRA = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")


def items_de(n):
    d = EPISODIOS[n]
    if d.get("repaso"):
        return [it for k in d["de"] for it in EPISODIOS[k]["items"]]
    return d["items"]


def limpio(t):
    return t.strip()


def mezclar(rng, correcta, distractores):
    ops = [correcta] + distractores
    rng.shuffle(ops)
    return ops, ops.index(correcta)


def main():
    pool = [it for n in EPISODIOS for it in (EPISODIOS[n]["items"] if not EPISODIOS[n].get("repaso") else [])]
    pool_eu = sorted({limpio(e) for e, s, _ in pool})
    pool_es = sorted({limpio(s) for e, s, _ in pool})
    palabras = sorted({w for e, _, _ in pool for w in PALABRA.findall(e) if len(w) >= 3 and not w[0].isupper()})
    out = {}
    for n in sorted(EPISODIOS):
        rng = random.Random(1000 + n)
        items = items_de(n)
        # un test por frase (alterna sentido), hasta 6; luego huecos, hasta 4
        orden = items[:]
        rng.shuffle(orden)
        tests, huecos = [], []
        for i, (eu, es, _) in enumerate(orden[:6]):
            eu, es = limpio(eu), limpio(es)
            if i % 2 == 0:
                cand = [x for x in pool_es if x != es]
                dist = rng.sample(cand, 3)
                ops, c = mezclar(rng, es, dist)
                tests.append({"t": "test", "p": f"Elige el significado de «{eu}»", "o": ops, "c": c})
            else:
                cand = [x for x in pool_eu if x != eu]
                dist = rng.sample(cand, 3)
                ops, c = mezclar(rng, eu, dist)
                tests.append({"t": "test", "p": f"Elige cómo se dice en euskera «{es}»", "o": ops, "c": c})
        for eu, es, _ in orden:
            if len(huecos) >= 4:
                break
            eu, es = limpio(eu), limpio(es)
            cands = [w for w in PALABRA.findall(eu) if len(w) >= 4 and not w[0].isupper()]
            if not cands:
                continue
            w = rng.choice(cands)
            frase = re.sub(r"\b" + re.escape(w) + r"\b", "_____", eu, count=1)
            dist = rng.sample([x for x in palabras if x != w and abs(len(x) - len(w)) <= 3], 2)
            ops, c = mezclar(rng, w, dist)
            huecos.append({"t": "hueco", "p": frase, "s": es, "o": ops, "c": c})
        # intercalar: test, test, hueco, ...
        preg, ti, hi = [], 0, 0
        while ti < len(tests) or hi < len(huecos):
            for _ in range(2):
                if ti < len(tests):
                    preg.append(tests[ti]); ti += 1
            if hi < len(huecos):
                preg.append(huecos[hi]); hi += 1
        out[str(n)] = preg
    Path("ejercicios.json").write_text(json.dumps({"A1": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    print({k: len(v) for k, v in out.items()})


if __name__ == "__main__":
    main()
