"""Tono de los guiones: cercano, con humor suave y situaciones de la vida diaria. Texto propio.

ESCENAS: n -> (escena con la que arranca el episodio, encargo para el paseo).
Todo va en espanol, porque lo lee la voz en espanol.
"""

ESCENAS = {
    # A1
    2: ("Imagina que tu vecino aparca un coche reluciente delante de casa. Antes de preguntar cuánto le ha costado, vas a querer comentarlo.", "Cuando salgas hoy, fíjate en tres cosas de la calle y di en voz baja si son grandes, pequeñas, nuevas o viejas."),
    3: ("Llegas al bar del pueblo y hay una cara nueva. Toca preguntar quién es, de dónde viene y a qué se dedica, sin parecer un policía.", "La próxima vez que veas a un conocido, salúdale en euskera. Lo peor que puede pasar es que te invite a un café."),
    5: ("Tu nieto te enseña fotos de coches, y tú quieres saber cómo es de verdad y de qué color, que en la foto salen todos iguales.", "Por el camino, mira los coches aparcados y ve diciendo de qué color son. Eso sí, por lo bajo, que te van a mirar raro."),
    6: ("En cualquier sobremesa acaba saliendo la misma pregunta: y tú, ¿dónde vives? Hoy la vas a poder responder sin pensarlo.", "Piensa en tres amigos tuyos y di en voz alta dónde vive cada uno."),
    7: ("Suena el teléfono, y lo primero que te preguntan siempre es dónde estás. Como si fueras a estar en la luna.", "Hoy, cada vez que cambies de sitio, di dónde estás. En la cocina, en la calle, en el bar, lo que toque."),
    9: ("Entras en casa, ves una cara seria y hay que averiguar cómo está el ambiente antes de abrir la boca.", "Esta noche, antes de dormir, di cómo estás. Contento, cansado, o las dos cosas."),
    10: ("Hay un coche tapando tu garaje y alguien tiene que ser el dueño. Hoy aprendemos a preguntarlo.", "Mira las fotos de casa y di de quién es cada cosa."),
    11: ("En toda casa aparece un paraguas que nadie reconoce. Hoy vamos a aclarar de quién es cada cosa.", "Coge tres cosas de casa y di de quién son. Si son tuyas, mejor."),
    13: ("Has perdido las llaves otra vez. Siempre están encima, debajo o detrás de algo, así que hoy aprendemos justo eso.", "Cuando pierdas algo, búscalo en euskera: encima de la mesa, debajo de la silla, dentro de la bolsa."),
    14: ("Hay gente a la que le encanta contar todo lo que tiene. Hoy te preparamos para estar a su altura.", "Haz inventario de lo que llevas encima ahora mismo. Una llave, un móvil y unas ganas de sentarte."),
    15: ("Y en la otra cara de la moneda está el que no tiene ni coche, ni dinero, ni ganas. Hoy toca decir lo que no se tiene.", "Piensa en tres cosas que no tienes y dilas en voz alta. Un yate, por ejemplo."),
    17: ("Sales de casa y siempre hay alguien que te pregunta a dónde vas. Hoy ya tienes respuesta.", "Mientras andas, di en voz alta a dónde vas. Al parque, a la tienda, o a ninguna parte, que también vale."),
    18: ("A veces no vas a un sitio sino a ver a alguien: al médico, a la abuela, al amigo de siempre. Y eso se dice de otra manera.", "Piensa a quién vas a ver esta semana y dilo en euskera."),
    19: ("Llegas a casa y te preguntan de dónde vienes, con esa mirada de quien ya sabe la respuesta.", "Cuando vuelvas del paseo, di de dónde vienes antes de quitarte los zapatos."),
    21: ("Nunca se va a casa de alguien con las manos vacías. Hoy aprendemos a decir qué traemos y para quién.", "La próxima vez que le lleves algo a alguien, dile en euskera para quién es."),
    22: ("Traer y llevar parecen lo mismo hasta que te equivocas. Y después, vamos a contar lo que ya hemos hecho hoy.", "Antes de cenar, cuenta tres cosas que ya has hecho hoy."),
    23: ("Estás en el mercado, te dicen el precio y se te escapa una exclamación. Hoy aprendemos a exclamar, a preguntar cuánto vale y a decir lo que quieres.", "En la próxima compra, piensa cómo preguntarías el precio. Y cómo pondrías el grito en el cielo."),
    # A2
    25: ("Te llaman a mala hora, justo cuando estás con las manos en la masa. Hoy aprendemos a decir qué estás haciendo ahora mismo.", "Durante el paseo, ve contando lo que estás haciendo y qué tiempo hace. Que llueve, pues que llueve."),
    26: ("El lunes por la mañana siempre te preguntan qué hiciste el fin de semana. Hoy preparamos la respuesta, aunque solo vieras la tele.", "Cuenta en voz alta tres cosas que hiciste ayer."),
    27: ("Hacer planes es muy fácil, lo difícil es cumplirlos. Hoy aprendemos a contar qué haremos mañana y con quién.", "Di qué vas a hacer mañana y con quién. Luego ya veremos si lo cumples."),
    29: ("Todos tenemos costumbres: el café de siempre, a la misma hora, en la misma silla. Hoy hablamos de lo que haces cada día.", "Cuenta tu rutina de la mañana, paso a paso."),
    30: ("En un pueblo siempre hay alguien que te ha visto. Hoy aprendemos a decir quién ha visto a quién, y qué puedes y qué no puedes hacer.", "Piensa a quién has visto hoy y dilo. Y luego, una cosa que puedes hacer y otra que ya no."),
    31: ("En cuanto se juntan dos abuelos empieza la competición: mi nieto es más alto que el tuyo. Hoy aprendemos a comparar.", "Compara dos cosas que veas por el camino. Este árbol es más alto que aquel, y así."),
    33: ("Cuando te encuentras a alguien, la pregunta de siempre es en qué andas. Y luego, si sabes algo del tema.", "Piensa en algo que sabes hacer muy bien, y en algo que no sabes ni por asomo."),
    34: ("Lo mejor de toda conversación: contar lo que ha dicho otro. Hoy aprendemos a decir que alguien ha dicho algo, y qué creemos nosotros.", "Cuenta lo último que te han dicho hoy, empezando por quién lo dijo."),
    35: ("Que si me gusta esto, que si se me ha olvidado lo otro. Hoy hablamos de lo que nos gusta y de lo que nos pasa sin querer.", "Di tres cosas que te gustan y una que se te olvida siempre."),
    37: ("Cuando eras joven todo era distinto, eso ya lo sabemos. Hoy aprendemos a contarlo en euskera.", "Cuenta dónde vivías de joven y en qué trabajabas. Aquí tienes público."),
    38: ("Hay casas donde se pide por favor, y casas donde se manda. Hoy aprendemos las dos cosas.", "Manda algo a alguien en euskera. Con cariño, que luego hay que convivir."),
    39: ("A veces hay que concretar: no cualquier libro, sino el que compraste ayer. Hoy aprendemos a precisar.", "Busca algo que compraste hace poco y descríbelo así: el libro que compré, la silla que arreglé."),
    41: ("Siempre hay un motivo, y si no, se inventa. Hoy aprendemos a preguntar por qué y a dar explicaciones.", "Piensa una buena excusa para llegar tarde. La vas a necesitar."),
    42: ("Llueve, estás cansado, y aun así sales a andar. Para eso sirve lo de hoy: para decir aunque.", "Piensa en algo que haces aunque no te apetezca nada."),
    43: ("Dar, decir, escribir, traer: siempre hay alguien que recibe. Hoy el verbo se complica un poco, pero se puede con él.", "Piensa qué le has dado o dicho hoy a alguien, y dilo."),
    45: ("A Bilbao se puede ir en tren, en autobús o andando, si tienes paciencia. Hoy aprendemos a decir cómo se hacen las cosas.", "Di cómo has venido hoy, y en qué idioma hablas con tus amigos."),
    46: ("Pasear es bueno, fumar es malo, y madrugar es un castigo. Hoy hablamos de las acciones como si fueran cosas.", "Di qué te gusta hacer, y qué es lo que no soportas."),
    # B1
    48: ("Nosotros los vascos, nosotros los abuelos, tú y yo. Hoy aprendemos a meternos en el grupo.", "Habla de tu cuadrilla usando nosotros."),
    49: ("Aquí llega uno de los secretos del euskera: lo importante se pone justo delante del verbo. Cambias el orden y cambias lo que dices.", "Responde hoy a una pregunta poniendo lo importante justo antes del verbo."),
    50: ("Hay palabras que ya traen la a de casa, y conviene no ponerles otra. Es un detalle pequeño que delata al que está aprendiendo.", "Busca palabras que ya acaben en a, como tienda o iglesia, y úsalas en una frase."),
    51: ("Hoy subimos un escalón. Vamos a aprender la forma más cuidada de decir que se puede hacer algo, la que queda bien delante del cura.", "Di tres cosas que puedes hacer hoy, con la forma que acabamos de ver."),
    53: ("El orden de las cosas importa: primero el café, después el periódico, y mientras tanto la radio.", "Cuenta tu mañana con antes, mientras y después."),
    54: ("¿Hasta dónde llega el paseo de hoy? Y además, vamos a distinguir lo mismo de lo igual, que no es lo mismo.", "Al volver, di hasta dónde has llegado."),
    55: ("No lo sé, quizá, seguramente. Lo que decimos todos cuando no queremos comprometernos. Hoy aprendemos a decirlo bien.", "Responde hoy a algo con un quizá, y quédate tan ancho."),
    57: ("Que venga, que se vaya, que lo haga otro. Hoy toca mandar sin estar delante.", "Di qué te gustaría que hiciera alguien. Que venga tu nieto a verte, por ejemplo."),
    58: ("Qué bonito, qué frío, vaya día. Y, ya puestos, la fecha en que naciste.", "Di tu fecha de nacimiento, y exclama algo sobre el tiempo de hoy."),
    59: ("Ni café ni té, tanto uno como otro, llueva o haga sol. Hoy aprendemos a unir ideas como los que ya saben.", "Di algo que haces llueva o haga sol."),
    61: ("No es lo mismo mucha gente que mucho calor. Se dice distinto, y hoy vas a saber cómo.", "Di qué tiempo hace hoy, y si hay mucha gente por la calle."),
    62: ("Hoy pensamos en alguien, y contamos en orden: primero, segundo, tercero.", "Di en quién has pensado hoy, y en qué piso vive."),
    63: ("Si llueve, me quedo en casa. Si no llueve, ya veremos. Hoy hablamos de condiciones.", "Haz un plan para mañana que empiece por si."),
    # B2
    65: ("Si te tocara la lotería. Todos hemos hecho planes con ese dinero. Hoy aprendemos a contarlos.", "Cuenta qué harías si fueras rico. Aquí no te oye el banco."),
    66: ("Si lo supiera, te lo diría. Seguimos con lo imaginario, que es gratis.", "Piensa en algo que harías si tuvieras más tiempo."),
    67: ("Dicen que, parece ser, a saber dónde estará. Hoy el chismorreo se convierte en gramática.", "Cuenta un rumor inofensivo, de esos de pueblo."),
    69: ("Nada, un poco, bastante, muchísimo. Hoy aprendemos a graduar lo que sentimos.", "Di cuánto te gusta algo, desde nada hasta muchísimo."),
    70: ("Lo he hecho yo mismo, y lo he hecho por ti. Hoy toca presumir un poco.", "Di algo que hayas hecho tú mismo, y por quién."),
    71: ("Hacia dónde vas, y cómo hacer que otro haga las cosas. Muy útil con los nietos.", "Piensa qué le has hecho hacer hoy a alguien."),
    73: ("Para qué has venido, y cualquier cosa vale. Hoy hablamos de para qué sirven las cosas.", "Di para qué sales a pasear."),
    74: ("Según dicen, según parece. Hoy aprendemos a contar las cosas sin hacernos responsables.", "Cuenta una noticia empezando por según he oído."),
    75: ("Tan alto como tu hermano, y come tanto como quieras. Comparaciones de igual a igual.", "Compárate con alguien, y que gane el mejor."),
    77: ("Qué te parece. Con esa pregunta empiezan todas las discusiones buenas.", "Da tu opinión sobre algo que hayas visto hoy."),
    78: ("Cada vez mejor, cuanto antes mejor. Y cuanto más se escucha, más se sabe.", "Di algo que cada vez te sale mejor."),
    79: ("Último esfuerzo, y este va de sonar bien: el acento, y esa hache que se escribe pero casi no suena.", "Repite despacio las palabras que más te cuesten. Aquí ya solo falta sacar pecho."),
}

ANIMO = [
    "Camina tranquilo y repite en voz alta cuando te toque. Si te equivocas, no pasa nada.",
    "Tú a tu ritmo. Y si alguien te mira raro por hablar solo, dile que estás estudiando.",
    "Repite en voz alta sin miedo. Aquí nadie va a corregirte, y menos los pájaros.",
    "Sin prisas. Lo importante es que te suene y que te atrevas a decirlo.",
]
PRESENTA = ["Esta frase significa", "Escucha cómo se dice", "Ahora, para decir", "Y esta otra significa"]
REPASITO = ["Repasamos las últimas.", "A ver si siguen ahí las últimas.", "Las tres últimas, una vez más.", "Antes de seguir, las últimas."]
CONVERSA = [
    "Ahora escucha cómo sonaría esto en una conversación de verdad. Primero entera.",
    "Vamos a ver a dos personas usando esto en la calle. Primero entera.",
    "Esto en la vida real suena así. Escucha la conversación entera.",
]
CIERRE = [
    "Muy bien, aitona. Otro episodio al bolsillo.",
    "Se acabó por hoy, aitona. Y sin despeinarte.",
    "Muy bien, aitona. Poco a poco, y sin que nadie te lo haya pedido.",
    "Hasta aquí, aitona. Ya sabes un poco más que esta mañana.",
]
REPASO_INICIO = [
    "Hoy toca repasar, que lo aprendido se va si no se usa.",
    "Hoy no hay nada nuevo. Hoy vamos a comprobar lo que ya sabes, que es bastante.",
    "Hoy hacemos limpieza general de lo aprendido.",
]


def rota(lista, n):
    return lista[n % len(lista)]
