#!/usr/bin/env python3
"""Genera guiones/NN-*.md (episodios 02-80) a partir de los datos de abajo.

Los textos son propios; de Hiru solo se toma el programa de cada unidad (ver temas_hiru.py).
Revisar con una persona que hable euskera antes de publicar.

    python herramientas/crear_guiones.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from temas_hiru import ampliar  # noqa: E402

VOCABULARIO = json.loads(Path(__file__).with_name("vocabulario.json").read_text(encoding="utf-8"))
MARCA_VOC, FIN_VOC = "# Vocabulario", "# Fin del vocabulario"

UNIDADES = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
DECENAS = {30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta", 80: "ochenta"}
NUM = (["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce",
        "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte",
        "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete",
        "veintiocho", "veintinueve"]
       + [DECENAS[n - n % 10] + (f" y {UNIDADES[n % 10]}" if n % 10 else "") for n in range(30, 81)])

# item = (euskera, español, nota)   nota = None o lista de (idioma, texto)
# dialogo = lista de (euskera, español)
EPISODIOS = {
    1: dict(slug="ni-amaia-naiz", titulo="Ni Amaia naiz", repaso=False, items=[
        ("Kaixo!", "¡Hola!", None), ("Egun on.", "Buenos días.", None),
        ("Ni Amaia naiz.", "Yo soy Amaia.", None), ("Zu Mikel zara.", "Tú eres Mikel.", None),
        ("Hura Amaia da.", "Ella es Amaia.", None), ("Zer moduz?", "¿Qué tal?", None),
        ("Ondo, eskerrik asko.", "Bien, gracias.", None)],
        dialogo=[("Kaixo! Ni Amaia naiz.", "¡Hola! Yo soy Amaia."), ("Kaixo! Ni Mikel naiz.", "¡Hola! Yo soy Mikel."),
                 ("Zu Mikel zara.", "Tú eres Mikel."), ("Hura Amaia da. Agur!", "Ella es Amaia. ¡Adiós!")]),

    2: dict(slug="auto-hau-berria-da", titulo="Este coche es nuevo", siguiente="cómo son las cosas",
        items=[
        ("Auto hau berria da.", "Este coche es nuevo.",
         [("ES", "En euskera la palabra para este va detrás del nombre. Primero se dice el coche, y después este.")]
         ),
        ("Auto hori zaharra da.", "Ese coche es viejo.", [("ES", "Para decir ese se usa otra palabra distinta.")]),
        ("Etxe hura handia da.", "Aquella casa es grande.", [("ES", "Y para decir aquel, algo más lejos, se usa una tercera palabra.")]),
        ("Mahai hau txikia da.", "Esta mesa es pequeña.", None),
        ("Liburu hau polita da.", "Este libro es bonito.", None),
        ("Gela hori zuria da.", "Esa habitación es blanca.", None),
        ("Auto hau berria da?", "¿Este coche es nuevo?", None),
        ],
        dialogo=[("Auto hau berria da.", "Este coche es nuevo."), ("Bai, berria da.", "Sí, es nuevo."),
                 ("Eta auto hori?", "¿Y ese coche?"), ("Hori zaharra da.", "Ese es viejo.")]),

    3: dict(slug="nor-zara-zu", titulo="¿Quién eres tú? Yo soy Xabi, de Zarautz", siguiente="cómo es el coche",
        items=[
        ("Nor zara zu?", "¿Quién eres tú?", None),
        ("Ni Xabi naiz.", "Yo soy Xabi.", [("ES", "Fíjate en la equis de Xabi. En euskera suena como una che suave, casi sh. Se dice sháhbi.")]),
        ("Zarauzkoa naiz.", "Soy de Zarautz.", [("ES", "Para decir de dónde eres se añade al nombre del lugar el final koa.")]),
        ("Donostiakoa naiz.", "Soy de San Sebastián.", None),
        ("Bilbokoa naiz.", "Soy de Bilbao.", None),
        ("Nongoa zara?", "¿De dónde eres?", None),
        ("Eta zu?", "¿Y tú?", None),
        ],
        dialogo=[("Kaixo! Nor zara zu?", "¡Hola! ¿Quién eres tú?"), ("Ni Xabi naiz. Zarauzkoa naiz. Eta zu?", "Yo soy Xabi. Soy de Zarautz. ¿Y tú?"),
                 ("Ni Amaia naiz. Donostiakoa naiz.", "Yo soy Amaia. Soy de San Sebastián."), ("Nongoa zara?", "¿De dónde eres?")]),

    5: dict(slug="nolakoa-da-autoa", titulo="¿Cómo es el coche?", siguiente="dónde vive Amaia",
        items=[
        ("Nolakoa da autoa?", "¿Cómo es el coche?", [("ES", "Hoy hablamos de cómo son las cosas. Cuando decimos el coche, sin la palabra este, el nombre termina en a.")]),
        ("Autoa handia da.", "El coche es grande.", None),
        ("Autoa txikia da.", "El coche es pequeño.", None),
        ("Autoa garestia da.", "El coche es caro.", None),
        ("Autoa merkea da.", "El coche es barato.", None),
        ("Autoa azkarra da.", "El coche es rápido.", None),
        ("Etxea polita da.", "La casa es bonita.", None),
        ],
        dialogo=[("Nolakoa da autoa?", "¿Cómo es el coche?"), ("Berria da, eta handia.", "Es nuevo, y grande."),
                 ("Garestia da?", "¿Es caro?"), ("Bai, garestia da.", "Sí, es caro.")]),

    6: dict(slug="amaia-donostian-bizi-da", titulo="Amaia vive en San Sebastián", siguiente="dónde está Amaia",
        items=[
        ("Non bizi zara?", "¿Dónde vives?", None),
        ("Zarautzen bizi naiz.", "Vivo en Zarautz.", [("ES", "Para decir en, se añade una n, o en, al final del nombre del lugar.")]),
        ("Donostian bizi naiz.", "Vivo en San Sebastián.", None),
        ("Amaia Donostian bizi da.", "Amaia vive en San Sebastián.", None),
        ("Mikel Bilbon bizi da.", "Mikel vive en Bilbao.", None),
        ("Non bizi da Amaia?", "¿Dónde vive Amaia?", None),
        ("Eta zu, non bizi zara?", "¿Y tú, dónde vives?", None),
        ],
        dialogo=[("Non bizi zara?", "¿Dónde vives?"), ("Donostian bizi naiz. Eta zu?", "Vivo en San Sebastián. ¿Y tú?"),
                 ("Ni Zarautzen bizi naiz.", "Yo vivo en Zarautz."), ("Mikel Bilbon bizi da.", "Mikel vive en Bilbao.")]),

    7: dict(slug="amaia-etxean-dago", titulo="Amaia está en casa", siguiente="cómo se siente Amaia",
        items=[
        ("Amaia etxean dago.", "Amaia está en casa.", [("ES", "Hoy aprendemos otro verbo, estar. Se usa para decir dónde está alguien.")]),
        ("Ni etxean nago.", "Yo estoy en casa.", None),
        ("Zu etxean zaude.", "Tú estás en casa.", None),
        ("Mikel kalean dago.", "Mikel está en la calle.", None),
        ("Amaia parkean dago.", "Amaia está en el parque.", None),
        ("Non dago Amaia?", "¿Dónde está Amaia?", None),
        ("Non zaude?", "¿Dónde estás?", None),
        ],
        dialogo=[("Kaixo, Amaia! Non zaude?", "¡Hola, Amaia! ¿Dónde estás?"), ("Etxean nago. Eta zu?", "Estoy en casa. ¿Y tú?"),
                 ("Ni kalean nago.", "Yo estoy en la calle."), ("Agur!", "¡Adiós!")]),

    9: dict(slug="amaia-haserre-dago", titulo="Amaia está enfadada", siguiente="de quién es el coche",
        items=[
        ("Zer moduz zaude?", "¿Cómo estás?", [("ES", "Con el verbo estar también decimos cómo nos sentimos. Escucha cómo se pregunta.")]),
        ("Ondo nago.", "Estoy bien.", None),
        ("Amaia haserre dago.", "Amaia está enfadada.", None),
        ("Ni pozik nago.", "Yo estoy contento.", None),
        ("Zu nekatuta zaude.", "Tú estás cansado.", None),
        ("Mikel triste dago.", "Mikel está triste.", None),
        ("Ez nago ondo.", "No estoy bien.", [("ES", "Para decir que no, se pone delante del verbo la palabra ez.")]),
        ],
        dialogo=[("Zer moduz zaude, Amaia?", "¿Cómo estás, Amaia?"), ("Ez nago ondo. Nekatuta nago.", "No estoy bien. Estoy cansada."),
                 ("Triste zaude?", "¿Estás triste?"), ("Ez, haserre nago.", "No, estoy enfadada.")]),

    10: dict(slug="noren-autoa-da-hau", titulo="¿De quién es este coche?", siguiente="de quién es cada cosa",
        items=[
        ("Noren autoa da hau?", "¿De quién es este coche?", None),
        ("Hau Amaiaren autoa da.", "Este es el coche de Amaia.", [("ES", "Para decir de alguien, se añade ren al nombre si termina en vocal.")]),
        ("Hori Mikelen autoa da.", "Ese es el coche de Mikel.", [("ES", "Si el nombre termina en consonante, solo se añade en.")]),
        ("Hura Xabiren autoa da.", "Aquel es el coche de Xabi.", None),
        ("Hau nire autoa da.", "Este es mi coche.", None),
        ("Hori zure autoa da.", "Ese es tu coche.", None),
        ("Hau Amaiaren etxea da.", "Esta es la casa de Amaia.", None),
        ],
        dialogo=[("Noren autoa da hau?", "¿De quién es este coche?"), ("Hau Mikelen autoa da.", "Este es el coche de Mikel."),
                 ("Eta hura?", "¿Y aquel?"), ("Hura nire autoa da.", "Aquel es mi coche.")]),

    11: dict(slug="norena-da-auto-hau", titulo="¿De quién es este coche? Es de Amaia", siguiente="dónde está cada cosa",
        items=[
        ("Norena da auto hau?", "¿De quién es este coche?", [("ES", "Ahora una forma más corta. Ya no repetimos la palabra coche.")]),
        ("Amaiarena da.", "Es de Amaia.", None),
        ("Mikelena da.", "Es de Mikel.", None),
        ("Xabirena da.", "Es de Xabi.", None),
        ("Nirea da.", "Es mío.", None),
        ("Zurea da?", "¿Es tuyo?", None),
        ("Ez, ez da nirea.", "No, no es mío.", None),
        ],
        dialogo=[("Norena da liburu hau?", "¿De quién es este libro?"), ("Amaiarena da.", "Es de Amaia."),
                 ("Zurea da?", "¿Es tuyo?"), ("Ez, ez da nirea. Mikelena da.", "No, no es mío. Es de Mikel.")]),

    13: dict(slug="amaia-mikelen-ondoan-dago", titulo="Amaia está al lado de Mikel", siguiente="qué tiene Amaia",
        items=[
        ("Amaia Mikelen ondoan dago.", "Amaia está al lado de Mikel.", None),
        ("Mikel Amaiaren ondoan dago.", "Mikel está al lado de Amaia.", None),
        ("Autoa etxearen aurrean dago.", "El coche está delante de la casa.", None),
        ("Liburua mahaiaren gainean dago.", "El libro está sobre la mesa.", None),
        ("Gatua mahaiaren azpian dago.", "El gato está debajo de la mesa.", None),
        ("Non dago liburua?", "¿Dónde está el libro?", None),
        ("Non dago gatua?", "¿Dónde está el gato?", None),
        ],
        dialogo=[("Non dago liburua?", "¿Dónde está el libro?"), ("Mahaiaren gainean dago.", "Está sobre la mesa."),
                 ("Eta gatua?", "¿Y el gato?"), ("Gatua mahaiaren azpian dago.", "El gato está debajo de la mesa.")]),

    14: dict(slug="amaiak-liburu-bat-dauka", titulo="Amaia tiene un libro", siguiente="lo que no se tiene",
        items=[
        ("Amaiak liburu bat dauka.", "Amaia tiene un libro.", [("ES", "Para decir tener, se usa un verbo nuevo, y el nombre de quien tiene lleva una k al final.")]),
        ("Mikelek auto bat dauka.", "Mikel tiene un coche.", None),
        ("Nik liburu bat daukat.", "Yo tengo un libro.", None),
        ("Zuk auto bat daukazu.", "Tú tienes un coche.", None),
        ("Amaiak gatu bat dauka.", "Amaia tiene un gato.", None),
        ("Zer daukazu?", "¿Qué tienes?", None),
        ("Eta zuk?", "¿Y tú?", None),
        ],
        dialogo=[("Zer daukazu?", "¿Qué tienes?"), ("Liburu bat daukat. Eta zuk?", "Tengo un libro. ¿Y tú?"),
                 ("Nik gatu bat daukat.", "Yo tengo un gato."), ("Amaiak auto bat dauka.", "Amaia tiene un coche.")]),

    15: dict(slug="neska-horrek-ez-dauka-libururik", titulo="Esa chica no tiene libros", siguiente="a dónde va Amaia",
        items=[
        ("Neska horrek ez dauka libururik.", "Esa chica no tiene libros.", [("ES", "Para decir que no se tiene algo, se pone ez delante del verbo, y el nombre termina en rik.")]),
        ("Mutil horrek ez dauka autorik.", "Ese chico no tiene coche.", None),
        ("Nik ez daukat libururik.", "Yo no tengo libros.", None),
        ("Zuk ez daukazu autorik.", "Tú no tienes coche.", None),
        ("Amaiak ez dauka gaturik.", "Amaia no tiene gato.", None),
        ("Zuk liburu bat daukazu?", "¿Tienes un libro?", None),
        ("Bai, liburu bat daukat.", "Sí, tengo un libro.", None),
        ],
        dialogo=[("Zuk liburu bat daukazu?", "¿Tienes un libro?"), ("Ez, nik ez daukat libururik.", "No, yo no tengo libros."),
                 ("Eta neska horrek?", "¿Y esa chica?"), ("Neska horrek liburu bat dauka.", "Esa chica tiene un libro.")]),

    17: dict(slug="amaia-dendara-doa", titulo="Amaia va a la tienda", siguiente="ir a casa de la abuela",
        items=[
        ("Nora zoaz?", "¿A dónde vas?", None),
        ("Dendara noa.", "Voy a la tienda.", [("ES", "Para decir a un lugar, se añade ra al final.")]),
        ("Amaia dendara doa.", "Amaia va a la tienda.", None),
        ("Mikel parkera doa.", "Mikel va al parque.", None),
        ("Ni etxera noa.", "Yo voy a casa.", None),
        ("Zu kalera zoaz.", "Tú vas a la calle.", None),
        ("Eta zu, nora zoaz?", "Y tú, ¿a dónde vas?", None),
        ],
        dialogo=[("Kaixo! Nora zoaz?", "¡Hola! ¿A dónde vas?"), ("Dendara noa. Eta zu?", "Voy a la tienda. ¿Y tú?"),
                 ("Ni parkera noa.", "Yo voy al parque."), ("Agur!", "¡Adiós!")]),

    18: dict(slug="amaia-amonarengana-joan-da", titulo="Amaia ha ido a casa de su abuela", siguiente="de dónde viene Amaia",
        items=[
        ("Amaia amonarengana joan da.", "Amaia ha ido a ver a su abuela.", [("ES", "Cuando vamos hacia una persona, no hacia un lugar, se añade arengana, o engana con nombres propios que acaban en consonante. Abuela se dice amona.")]),
        ("Mikel aitonarengana joan da.", "Mikel ha ido a ver a su abuelo.", None),
        ("Ni amonarengana joan naiz.", "Yo he ido a ver a la abuela.", None),
        ("Zu Amaiarengana joan zara.", "Tú has ido a ver a Amaia.", None),
        ("Nora joan da Amaia?", "¿A dónde ha ido Amaia?", None),
        ("Amonarengana joan da.", "Ha ido a ver a la abuela.", None),
        ],
        dialogo=[("Non dago Amaia?", "¿Dónde está Amaia?"), ("Amonarengana joan da.", "Ha ido a ver a su abuela."),
                 ("Eta Mikel?", "¿Y Mikel?"), ("Mikel aitonarengana joan da.", "Mikel ha ido a ver a su abuelo.")]),

    19: dict(slug="amaia-amonaren-etxetik-dator", titulo="Amaia viene de casa de la abuela", siguiente="traer una manzana",
        items=[
        ("Amaia amonaren etxetik dator.", "Amaia viene de casa de la abuela.", [("ES", "Para decir desde un lugar, se añade tik al final.")]),
        ("Nondik zatoz?", "¿De dónde vienes?", None),
        ("Dendatik nator.", "Vengo de la tienda.", None),
        ("Mikel parketik dator.", "Mikel viene del parque.", None),
        ("Zu kaletik zatoz.", "Tú vienes de la calle.", None),
        ("Ni etxetik nator.", "Yo vengo de casa.", None),
        ],
        dialogo=[("Kaixo, Mikel! Nondik zatoz?", "¡Hola, Mikel! ¿De dónde vienes?"), ("Dendatik nator. Eta zu, nora zoaz?", "Vengo de la tienda. ¿Y tú, a dónde vas?"),
                 ("Etxera noa.", "Voy a casa."), ("Agur!", "¡Adiós!")]),

    21: dict(slug="amaiak-sagar-bat-dakar", titulo="Amaia trae una manzana para su abuela", siguiente="llevar algo en la bolsa",
        items=[
        ("Amaiak sagar bat dakar.", "Amaia trae una manzana.", [("ES", "Sagar significa manzana. Y el verbo traer cambia según quién traiga.")]),
        ("Amaiak sagar bat dakar bere amonarentzat.", "Amaia trae una manzana para su abuela.", [("ES", "Para decir para alguien se añade arentzat. Bere significa su.")]),
        ("Nik liburu bat dakart zuretzat.", "Yo traigo un libro para ti.", None),
        ("Zuk sagar bat dakarzu niretzat.", "Tú traes una manzana para mí.", None),
        ("Mikelek ogia dakar Amaiarentzat.", "Mikel trae el pan para Amaia.", None),
        ("Zer dakarzu?", "¿Qué traes?", None),
        ],
        dialogo=[("Kaixo, amona! Sagar bat dakart zuretzat.", "¡Hola, abuela! Traigo una manzana para ti."), ("Eskerrik asko, Amaia!", "¡Muchas gracias, Amaia!"),
                 ("Zer dakar Mikelek?", "¿Qué trae Mikel?"), ("Mikelek ogia dakar.", "Mikel trae el pan.")]),

    22: dict(slug="amaiak-sagar-bat-darama-poltsan", titulo="Amaia lleva una manzana en la bolsa", siguiente="una exclamación",
        items=[
        ("Amaiak sagar bat darama poltsan.", "Amaia lleva una manzana en la bolsa.", [("ES", "Hay dos verbos parecidos. Traer, que es llegar con algo, y llevar, que es ir con algo. Poltsa significa bolsa, y con n final, en la bolsa.")]),
        ("Nik liburu bat daramat poltsan.", "Yo llevo un libro en la bolsa.", None),
        ("Zuk zer daramazu poltsan?", "¿Qué llevas tú en la bolsa?", None),
        ("Mikelek ogia darama poltsan.", "Mikel lleva el pan en la bolsa.", None),
        ("Poltsa handia da.", "La bolsa es grande.", None),
        ("Poltsa txikia da.", "La bolsa es pequeña.", None),
        ],
        dialogo=[("Zer daramazu poltsan?", "¿Qué llevas en la bolsa?"), ("Sagar bat daramat. Eta zuk?", "Llevo una manzana. ¿Y tú?"),
                 ("Nik ogia daramat.", "Yo llevo el pan."), ("Poltsa handia da.", "La bolsa es grande.")]),

    23: dict(slug="bai-auto-garestia", titulo="¡Qué coche tan caro!", siguiente="un repaso final",
        items=[
        ("Bai auto garestia!", "¡Qué coche tan caro!", [("ES", "Para exclamar, qué coche tan caro, la frase empieza con una palabra especial.")]),
        ("Bai etxe handia!", "¡Qué casa tan grande!", None),
        ("Bai neska polita!", "¡Qué chica tan bonita!", None),
        ("Bai gatu txikia!", "¡Qué gato tan pequeño!", None),
        ("Bai liburu zaharra!", "¡Qué libro tan viejo!", None),
        ("Begira!", "¡Mira!", None),
        ("Baina garestia da.", "Pero es caro.", None),
        ],
        dialogo=[("Begira, Amaia! Bai auto berria!", "¡Mira, Amaia! ¡Qué coche tan nuevo!"), ("Bai, baina garestia da.", "Sí, pero es caro."),
                 ("Bai auto garestia!", "¡Qué coche tan caro!"), ("Eta handia da.", "Y es grande.")]),

    4: dict(slug="errepasoa-1", titulo="Repaso uno", repaso=True, de=[1, 2, 3], siguiente="cómo es el coche"),
    8: dict(slug="errepasoa-2", titulo="Repaso dos", repaso=True, de=[5, 6, 7], siguiente="cómo se siente Amaia"),
    12: dict(slug="errepasoa-3", titulo="Repaso tres", repaso=True, de=[9, 10, 11], siguiente="dónde está cada cosa"),
    16: dict(slug="errepasoa-4", titulo="Repaso cuatro", repaso=True, de=[13, 14, 15], siguiente="ir a sitios"),
    20: dict(slug="errepasoa-5", titulo="Repaso cinco", repaso=True, de=[17, 18, 19], siguiente="traer y llevar"),
    24: dict(slug="errepasoa-6", titulo="Repaso seis", repaso=True, de=[21, 22, 23], siguiente=None),
}
ampliar(EPISODIOS)


def pausa(eu):
    palabras = len(eu.replace("?", "").replace("!", "").split())
    return min(12, 3 + round(palabras * 1.5))


def es(t):
    return f"ES: {t}"


def eu(t):
    return f"EU: {t}"


def p(s):
    return f"[PAUSA {s}]"


def bloque_dialogo(dialogo, L):
    L += ["", es("Ahora escucha una conversación sencilla. Primero entera.")]
    for e, _ in dialogo:
        L += [eu(e), p(2)]
    L += ["", es("En español sería así.")]
    for _, s in dialogo:
        L += [es(s)]
    L += ["", es("Ahora la repetimos frase por frase. Repite en voz alta.")]
    for e, _ in dialogo:
        L += [eu(e), p(pausa(e) + 2)]


def bloque_vocabulario(n):
    """Lineas con las palabras de la leccion; las lineas # las ignora generar_podcast.py."""
    palabras = VOCABULARIO.get(str(n), [])
    if not palabras:
        return []
    L = [MARCA_VOC, es("Antes de terminar, vamos con el vocabulario de esta lección. Yo digo la palabra en español, la oyes en euskera, y tú la repites."), p(2), ""]
    for e, s in palabras:
        L += [es(s), eu(e), p(pausa(e)), eu(e), p(pausa(e)), ""]
    return L + [FIN_VOC, ""]


def episodio_nuevo(n, d):
    L = [f"# Episodio {n} - {d['titulo']} (guion propio; del curso de Hiru solo se toma el tema)", ""]
    L += [es(f"Kaixo, aitona. Bienvenido al episodio {NUM[n]} de Euskera paseando."),
          es("Hoy hablamos de esto: " + d["titulo"][0].lower() + d["titulo"][1:] + ("" if d["titulo"][-1] in ".?!" else ".")),
          es("Camina tranquilo y repite en voz alta cuando te toque. Si te equivocas, no pasa nada."), p(2), ""]
    items = d["items"]
    for i, (e, s, nota) in enumerate(items):
        if nota:
            for lang, t in nota:
                L.append(f"{lang}: {t}")
            L.append(es("Escucha la frase."))
        L += [es(f"Esta frase significa: {s}"), eu(e), p(3), es("Repite."), eu(e), p(pausa(e)), eu(e), p(pausa(e)), ""]
        if (i + 1) % 3 == 0 and i + 1 < len(items):
            L += [es("Repasamos las últimas.")]
            for e2, _, _ in items[i - 2:i + 1]:
                L += [eu(e2), p(pausa(e2))]
            L.append("")
    L += [es("Vamos a repasar todo lo de hoy una vez más, solo en euskera. Repite cada frase.")]
    for e, _, _ in items:
        L += [eu(e), p(pausa(e))]
    bloque_dialogo(d["dialogo"], L)
    L += ["", es("Y ahora el repaso final. Yo te digo la frase en español, tú la dices en euskera, y después oyes la respuesta correcta.")]
    for e, s, _ in items:
        L += [es(s), p(pausa(e) + 3), eu(e), p(2)]
    L += [""] + bloque_vocabulario(n)
    L += [es("Muy bien, aitona. Has terminado el episodio de hoy.")]
    if d.get("siguiente"):
        L.append(es(f"En el próximo episodio veremos {d['siguiente']}. Hasta pronto."))
    L.append(eu("Agur!"))
    return "\n".join(L) + "\n"


def episodio_repaso(n, d):
    fuentes = [EPISODIOS[k] for k in d["de"]]
    items = [it for f in fuentes for it in f["items"]]
    L = [f"# Episodio {n} - {d['titulo']} (guion propio; repaso de los episodios {d['de']})", ""]
    L += [es(f"Kaixo, aitona. Bienvenido al episodio {NUM[n]}. Hoy toca repasar lo que ya sabes."),
          es("Primero hacemos el juego de traducir. Y al final, las conversaciones."), p(2), ""]
    L += ["", es("Primera parte. Yo digo la frase en español, tú la dices en euskera, y luego oyes la respuesta.")]
    for e, s, _ in items:
        L += [es(s), p(pausa(e) + 3), eu(e), p(2)]
    L += ["", es("Segunda parte. Las conversaciones de estos episodios.")]
    for f in fuentes:
        L += [es(f"Conversación sobre: {f['titulo']}.")]
        for e, _ in f["dialogo"]:
            L += [eu(e), p(2)]
        L += [es("Ahora tú, frase por frase.")]
        for e, _ in f["dialogo"]:
            L += [eu(e), p(pausa(e) + 2)]
        L.append("")
    L += [es("Muy bien, aitona. Cada día sabes más.")]
    if d.get("siguiente"):
        L.append(es(f"En el próximo episodio veremos {d['siguiente']}. Hasta pronto."))
    else:
        L.append(es("Has llegado al final de esta serie. Zorionak, aitona. Eso quiere decir felicidades."))
    L.append(eu("Agur!"))
    return "\n".join(L) + "\n"


def main():
    out = Path(__file__).resolve().parent.parent / "guiones"
    out.mkdir(exist_ok=True)
    for n, d in sorted(EPISODIOS.items()):
        if n == 1:  # el 01 esta escrito a mano: solo se le pone el vocabulario antes de la despedida
            f = out / "01-ni-amaia-naiz.md"
            patron = re.escape(MARCA_VOC) + r".*?" + re.escape(FIN_VOC) + r"\n+"
            txt = re.sub(patron, "", f.read_text(encoding="utf-8"), flags=re.S)
            despedida = "ES: Muy bien, aitona. Hoy has"
            f.write_text(txt.replace(despedida, "\n".join(bloque_vocabulario(1)) + "\n" + despedida, 1), encoding="utf-8")
            continue
        txt = episodio_repaso(n, d) if d.get("repaso") else episodio_nuevo(n, d)
        (out / f"{n:02d}-{d['slug']}.md").write_text(txt, encoding="utf-8")
        print(n, d["slug"])


if __name__ == "__main__":
    main()
