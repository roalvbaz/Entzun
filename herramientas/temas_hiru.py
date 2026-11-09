"""Datos de los guiones segun lo que ensena cada leccion de Hiru (temas, gramatica y vocabulario).

Las frases y explicaciones son propias: de Hiru solo se toma el programa. Revisar con alguien que hable euskera.
item = (euskera, espanol) o (euskera, espanol, "explicacion en espanol")
"""

# Frases que faltaban en los episodios A1 para cubrir lo que ensena cada leccion.
A1_AMPLIAR = {
    2: [("Autoak berriak dira.", "Los coches son nuevos.", "El plural se forma terminando el nombre en ak. Y el adjetivo tambien va en plural."),
        ("Liburu bat daukat.", "Tengo un libro.", "Un o una se dice bat, y va detras del nombre."),
        ("Lagun batzuk etorri dira.", "Han venido unos amigos.", "Unos o unas se dice batzuk.")],
    3: [("Zer zara zu?", "¿Qué eres tú?", "Para preguntar la profesión se usa zer, que significa qué."),
        ("Irakaslea naiz.", "Soy profesor."), ("Arrantzalea naiz.", "Soy pescador."), ("Aspaldiko!", "¡Cuánto tiempo sin verte!"),
        ("Gero arte!", "¡Hasta luego!"), ("Bihar arte!", "¡Hasta mañana!")],
    5: [("Zein koloretakoa da autoa?", "¿De qué color es el coche?", "Para preguntar el color se dice zein koloretakoa."),
        ("Autoa gorria da.", "El coche es rojo."), ("Etxea zuria da.", "La casa es blanca."), ("Itsasoa urdina da.", "El mar es azul.")],
    6: [("Herri txiki batean bizi naiz.", "Vivo en un pueblo pequeño."), ("Hiri handi batean bizi gara.", "Vivimos en una ciudad grande."),
        ("Auzo honetan bizi naiz.", "Vivo en este barrio.")],
    7: [("Ama sukaldean dago.", "La madre está en la cocina."), ("Haurrak eskolan daude.", "Los niños están en la escuela."),
        ("Gu tabernan gaude.", "Nosotros estamos en el bar.")],
    9: [("Nola dago aitona?", "¿Cómo está el abuelo?", "Para preguntar cómo está alguien también se usa nola."),
        ("Eserita nago.", "Estoy sentado."), ("Atea itxita dago.", "La puerta está cerrada."), ("Gela garbi dago.", "La habitación está limpia.")],
    10: [("Hau nire amaren etxea da.", "Esta es la casa de mi madre."), ("Hori nire aitaren autoa da.", "Ese es el coche de mi padre."),
         ("Hura nire anaiaren semea da.", "Aquel es el hijo de mi hermano.")],
    11: [("Norena da gutun hau?", "¿De quién es esta carta?"), ("Gorbata hau aitarena da.", "Esta corbata es del padre."),
         ("Baloi hau mutilarena da.", "Este balón es del chico.")],
    13: [("Giltzak poltsaren barruan daude.", "Las llaves están dentro de la bolsa."), ("Autoa etxearen atzean dago.", "El coche está detrás de la casa."),
         ("Eliza udaletxearen eta banketxearen artean dago.", "La iglesia está entre el ayuntamiento y el banco.")],
    14: [("Guk etxe bat daukagu.", "Nosotros tenemos una casa."), ("Haiek hiru seme dauzkate.", "Ellos tienen tres hijos.", "Cuando lo que se tiene es plural, el verbo cambia un poco.")],
    17: [("Bilbora goaz.", "Vamos a Bilbao.", "Con nombres de lugares también se usa ra."), ("Dendetara noa.", "Voy a las tiendas.", "En plural se dice etara."),
         ("Hondartzara goaz.", "Vamos a la playa.")],
    18: [("Niregana zatoz.", "Vienes hacia mí.", "Con yo y tú se dice niregana y zuregana."), ("Medikuarengana noa.", "Voy al médico.")],
    19: [("Gu Bilbotik gatoz.", "Nosotros venimos de Bilbao."), ("Hondartzatik datoz.", "Vienen de la playa.")],
    21: [("Haurrentzat da.", "Es para los niños.", "Para varias personas se dice entzat."), ("Hau zuretzat da.", "Esto es para ti.")],
    22: [("Amaiak sagarra jan du.", "Amaia se ha comido la manzana.", "Para hablar de lo que ya está hecho, el que lo hace lleva k, y se termina con du."),
         ("Nik ogia erosi dut.", "Yo he comprado el pan."), ("Zuk zer egin duzu?", "¿Tú qué has hecho?"), ("Mikel etxera joan da.", "Mikel se ha ido a casa.", "Con verbos como ir, en vez de du se dice da.")],
    23: [("Zenbat balio du?", "¿Cuánto vale?", "Para preguntar el precio se usa el verbo balio."), ("Hamar euro balio du.", "Vale diez euros."),
         ("Zer nahi duzu?", "¿Qué quieres?", "Querer se dice nahi."), ("Kafe bat nahi dut.", "Quiero un café."), ("Auto berri bat nahi dut.", "Quiero un coche nuevo.")],
}

# n: (slug, titulo, lo que se anuncia al final del episodio anterior, items, dialogo)
NUEVOS = {
    # ---------------- A2 ----------------
    25: ("zer-egiten-ari-zara", "Qué estás haciendo ahora", "lo que estás haciendo ahora", [
        ("Zer egiten ari zara?", "¿Qué estás haciendo?", "Para decir que algo está pasando justo ahora, el verbo termina en ten o tzen, y detrás se pone la palabra ari."),
        ("Ogia egiten ari naiz.", "Estoy haciendo pan."), ("Aitona egunkaria irakurtzen ari da.", "El abuelo está leyendo el periódico."),
        ("Mikel lanean ari da.", "Mikel está trabajando."), ("Haurrak jolasten ari dira.", "Los niños están jugando."),
        ("Euskara ikasten ari gara.", "Estamos aprendiendo euskera."), ("Euria ari du.", "Está lloviendo.", "Para el tiempo se dice así, y es muy útil al salir a pasear."), ("Elurra ari du.", "Está nevando.")],
     [("Kaixo, aitona! Zer egiten ari zara?", "¡Hola, abuelo! ¿Qué estás haciendo?"), ("Egunkaria irakurtzen ari naiz. Eta zu?", "Estoy leyendo el periódico. ¿Y tú?"),
      ("Ni ogia egiten ari naiz.", "Yo estoy haciendo pan."), ("Kanpoan euria ari du.", "Fuera está lloviendo.")]),
    26: ("atzo-zer-egin-zenuen", "Lo que hiciste ayer", "lo que hiciste ayer", [
        ("Larunbatean mendira joan nintzen.", "El sábado fui al monte.", "Para hablar de un pasado ya terminado, naiz se convierte en nintzen."),
        ("Atzo etxean egon nintzen.", "Ayer estuve en casa."), ("Igandean Bilbora joan ginen.", "El domingo fuimos a Bilbao."), ("Mikel atzo etorri zen.", "Mikel vino ayer."),
        ("Atzo liburu bat erosi nuen.", "Ayer compré un libro.", "Y dut se convierte en nuen."), ("Amaiak ogia erosi zuen.", "Amaia compró el pan."),
        ("Zuk zer egin zenuen atzo?", "¿Tú qué hiciste ayer?"), ("Iaz Donostian bizi izan nintzen.", "El año pasado viví en San Sebastián.")],
     [("Zer egin zenuen larunbatean?", "¿Qué hiciste el sábado?"), ("Mendira joan nintzen.", "Fui al monte."), ("Norekin?", "¿Con quién?"), ("Bakarrik. Eta zuk?", "Solo. ¿Y tú?"), ("Nik liburu bat irakurri nuen.", "Yo leí un libro.")]),
    27: ("bihar-joango-naiz", "Lo que harás mañana y con quién", "el futuro y con quién hacemos las cosas", [
        ("Bihar Bilbora joango naiz.", "Mañana iré a Bilbao.", "Para hablar del futuro, se añade go o ko al verbo."),
        ("Etzi etorriko da.", "Pasado mañana vendrá."), ("Nik bihar ogia erosiko dut.", "Yo mañana compraré el pan."), ("Zuk zer egingo duzu igandean?", "¿Tú qué harás el domingo?"),
        ("Norekin joango zara?", "¿Con quién irás?", "Con alguien se dice añadiendo rekin o ekin."), ("Aitarekin joango naiz.", "Iré con mi padre."), ("Lagunekin joango naiz.", "Iré con los amigos."), ("Amonarekin egongo naiz.", "Estaré con la abuela.")],
     [("Bihar zer egingo duzu?", "¿Mañana qué harás?"), ("Bilbora joango naiz.", "Iré a Bilbao."), ("Norekin joango zara?", "¿Con quién irás?"), ("Aitarekin joango naiz.", "Iré con mi padre.")]),
    29: ("egunero-joaten-naiz", "Lo que haces cada día", "lo que haces cada día", [
        ("Egunero oinez ibiltzen naiz.", "Todos los días ando a pie.", "Para lo que se hace habitualmente, el verbo termina en ten o tzen, seguido de naiz o dut."),
        ("Astero joaten naiz azokara.", "Cada semana voy al mercado."), ("Goizero ogia erosten dut.", "Todas las mañanas compro el pan."), ("Batzuetan kafea hartzen dut.", "A veces tomo café."),
        ("Inoiz ez dut telebista ikusten.", "Nunca veo la televisión."), ("Igandeetan lagunekin bazkaltzen dut.", "Los domingos como con los amigos."),
        ("Urtean behin joaten naiz Bilbora.", "Voy a Bilbao una vez al año."), ("Noiz joaten zara hondartzara?", "¿Cuándo vas a la playa?")],
     [("Egunero ibiltzen zara?", "¿Andas todos los días?"), ("Bai, goizero ibiltzen naiz.", "Sí, ando todas las mañanas."), ("Eta azokara?", "¿Y al mercado?"), ("Astero joaten naiz.", "Voy cada semana.")]),
    30: ("ikusi-nau-eta-ahal", "Quién ve a quién, y poder hacer algo", "quién ve a quién, y cómo decir que puedes", [
        ("Aitonak ikusi nau.", "El abuelo me ha visto.", "Cuando la acción recae sobre mí, se dice nau. Sobre ti, zaitu."),
        ("Nik zu ikusi zaitut.", "Yo te he visto a ti."), ("Zuk ni ikusi nauzu.", "Tú me has visto a mí."), ("Mikelek gu ikusi gaitu.", "Mikel nos ha visto."),
        ("Etorri ahal zara?", "¿Puedes venir?", "Poder se dice ahal, y va detrás del verbo."), ("Bai, etorri ahal naiz.", "Sí, puedo venir."),
        ("Liburu hau irakurri ahal dut?", "¿Puedo leer este libro?"), ("Ezin dut etorri.", "No puedo venir.", "Para no poder se dice ezin.")],
     [("Gaur ikusi zaitut kalean.", "Hoy te he visto en la calle."), ("Ni? Ez nauzu ikusi.", "¿A mí? No me has visto."), ("Bihar etorri ahal zara?", "¿Puedes venir mañana?"), ("Ez, ezin dut.", "No, no puedo.")]),
    31: ("handiagoa-baino", "Comparar: más grande que", "cómo comparar las cosas", [
        ("Nire etxea zure etxea baino handiagoa da.", "Mi casa es más grande que tu casa.", "Para decir más, el adjetivo termina en ago. Y que se dice baino."),
        ("Bilbo Donostia baino handiagoa da.", "Bilbao es más grande que San Sebastián."), ("Ni zu baino zaharragoa naiz.", "Yo soy mayor que tú."), ("Hau hori baino merkeagoa da.", "Esto es más barato que eso."),
        ("Mendia hondartza baino politagoa da.", "El monte es más bonito que la playa."), ("Zein da garestiena?", "¿Cuál es el más caro?", "Para el que más, el adjetivo termina en ena."),
        ("Hau da onena.", "Este es el mejor."), ("Zu bezain altua naiz.", "Soy tan alto como tú.")],
     [("Zein da garestiena?", "¿Cuál es el más caro?"), ("Hau hori baino garestiagoa da.", "Este es más caro que ese."), ("Baina handiagoa da.", "Pero es más grande."), ("Bai, eta onena da.", "Sí, y es el mejor.")]),
    33: ("ibili-eta-jakin", "Andar y saber", "los verbos andar y saber", [
        ("Zertan zabiltza?", "¿En qué andas?", "El verbo ibili significa andar, y también se usa para decir en qué estás metido."),
        ("Lanean nabil.", "Ando trabajando."), ("Mikel kalean dabil.", "Mikel anda por la calle."), ("Oinez gabiltza.", "Andamos a pie."),
        ("Badakit.", "Lo sé.", "Saber se dice jakin. Cuando afirmamos, se añade ba delante."), ("Ez dakit.", "No lo sé."), ("Badakizu euskaraz?", "¿Sabes euskera?"), ("Aitonak asko daki.", "El abuelo sabe mucho.")],
     [("Zertan zabiltza, aitona?", "¿En qué andas, abuelo?"), ("Euskara ikasten nabil.", "Ando aprendiendo euskera."), ("Badakizu asko?", "¿Sabes mucho?"), ("Ez dakit asko, baina ikasten ari naiz.", "No sé mucho, pero estoy aprendiendo.")]),
    34: ("esan-du-dela", "Decir y pensar que", "cómo decir que alguien ha dicho algo", [
        ("Aitonak ondo dagoela esan du.", "El abuelo ha dicho que está bien.", "El que del español se pega al final del verbo, como la."),
        ("Euria ari duela uste dut.", "Creo que está lloviendo."), ("Bihar etorriko dela esan du.", "Ha dicho que vendrá mañana."), ("Mikelek garestia dela dio.", "Mikel dice que es caro."),
        ("Badakit zu etxean zaudela.", "Sé que estás en casa."), ("Pozik nagoela esan dut.", "He dicho que estoy contento."), ("Ez dut uste etorriko denik.", "No creo que venga.", "Con no creo, en lugar de la se dice nik."), ("Zer esan du?", "¿Qué ha dicho?")],
     [("Zer esan du Mikelek?", "¿Qué ha dicho Mikel?"), ("Bihar etorriko dela esan du.", "Ha dicho que vendrá mañana."), ("Egia da?", "¿Es verdad?"), ("Ez dut uste etorriko denik.", "No creo que venga.")]),
    35: ("gustatzen-zait", "Lo que me gusta y lo que me pasa", "lo que nos gusta y lo que nos pasa", [
        ("Liburu hau gustatzen zait.", "Me gusta este libro.", "Me gusta se dice gustatzen zait. A ti, zaizu. A él, zaio."),
        ("Kafea gustatzen zaizu?", "¿Te gusta el café?"), ("Aitonari pilota gustatzen zaio.", "Al abuelo le gusta la pelota."), ("Niri ez zait gustatzen.", "A mí no me gusta."),
        ("Giltzak ahaztu zaizkit.", "Se me han olvidado las llaves.", "Si lo que pasa es plural, se dice zaizkit."), ("Autoa hondatu zait.", "Se me ha estropeado el coche."), ("Lagun bat etorri zait etxera.", "Me ha venido un amigo a casa."), ("Zer gertatu zaizu?", "¿Qué te ha pasado?")],
     [("Zer gertatu zaizu?", "¿Qué te ha pasado?"), ("Giltzak ahaztu zaizkit.", "Se me han olvidado las llaves."), ("Kafe bat nahi duzu?", "¿Quieres un café?"), ("Bai, kafea asko gustatzen zait.", "Sí, me gusta mucho el café.")]),
    37: ("gazte-nintzenean", "Cuando era joven", "cómo contar lo que pasaba antes", [
        ("Gazte nintzenean, Bilbon bizi nintzen.", "Cuando era joven, vivía en Bilbao.", "Para decir cuando, en el pasado, se añade enean al verbo."),
        ("Etxera nindoan.", "Iba a casa."), ("Amaia kalean zegoen.", "Amaia estaba en la calle."), ("Ni etxean nengoen euria hasi zenean.", "Yo estaba en casa cuando empezó a llover."),
        ("Autoa neukan.", "Tenía coche."), ("Ogia zekarren.", "Traía el pan."), ("Aitona etorri zenean, afaltzen ari ginen.", "Cuando vino el abuelo, estábamos cenando."), ("Zer zeneukan poltsan?", "¿Qué tenías en la bolsa?")],
     [("Non bizi zinen gazte zinenean?", "¿Dónde vivías cuando eras joven?"), ("Bilbon bizi nintzen.", "Vivía en Bilbao."), ("Autoa zeneukan?", "¿Tenías coche?"), ("Ez, oinez nindoan lanera.", "No, iba a pie al trabajo.")]),
    38: ("etorri-hona", "Dar órdenes y pedir cosas", "cómo dar órdenes y pedir cosas", [
        ("Etorri hona!", "¡Ven aquí!", "La forma más sencilla de mandar es decir el verbo solo."), ("Etor zaitez hona!", "¡Ven aquí!", "Y esta otra forma es un poco más completa."),
        ("Zoaz etxera!", "¡Vete a casa!"), ("Egon hor!", "¡Quédate ahí!"), ("Eseri hemen.", "Siéntate aquí."), ("Ekarri ura, mesedez.", "Trae agua, por favor."),
        ("Bilboko autobusa da.", "Es el autobús de Bilbao.", "La terminación ko indica de dónde o de cuándo es algo."), ("Etxeko giltzak non daude?", "¿Dónde están las llaves de casa?")],
     [("Etorri hona, aitona!", "¡Ven aquí, abuelo!"), ("Zer gertatzen da?", "¿Qué pasa?"), ("Eseri hemen, mesedez.", "Siéntate aquí, por favor."), ("Ekarri ura, mesedez.", "Trae agua, por favor.")]),
    39: ("erosi-dudan-liburua", "El libro que he comprado", "cómo decir el libro que he comprado", [
        ("Erosi dudan liburua ona da.", "El libro que he comprado es bueno.", "El que va pegado al verbo, con una n final, y delante del nombre."),
        ("Atzo ikusi zenuen gizona nire osaba da.", "El hombre que viste ayer es mi tío."), ("Etorri den mutila Xabi da.", "El chico que ha venido es Xabi."), ("Hemen dagoen autoa nirea da.", "El coche que está aquí es mío."),
        ("Zurezko mahaia da.", "Es una mesa de madera.", "De qué material es algo se dice con zko."), ("Harrizko etxea da.", "Es una casa de piedra."), ("Urrezko eraztuna da.", "Es un anillo de oro."), ("Etxe zuri-zuria da.", "Es una casa blanquísima.", "Repetir el adjetivo lo refuerza.")],
     [("Nor da etorri den gizona?", "¿Quién es el hombre que ha venido?"), ("Nire osaba da.", "Es mi tío."), ("Eta hemen dagoen autoa?", "¿Y el coche que está aquí?"), ("Hori nirea da.", "Ese es mío.")]),
    41: ("zergatik-lako", "Por qué: porque", "cómo decir por qué", [
        ("Zergatik zaude haserre?", "¿Por qué estás enfadado?", "Por qué se dice zergatik. Y porque se pega al verbo, como lako."),
        ("Nekatuta nagoelako.", "Porque estoy cansado."), ("Ez naiz joan euria ari duelako.", "No he ido porque está lloviendo."), ("Berandu nator autobusa galdu dudalako.", "Vengo tarde porque he perdido el autobús."),
        ("Pozik nago zu etorri zarelako.", "Estoy contento porque has venido."), ("Zergatik ez duzu jan?", "¿Por qué no has comido?"), ("Goserik ez daukadalako.", "Porque no tengo hambre."), ("Amona triste dago Mikel joan delako.", "La abuela está triste porque Mikel se ha ido.")],
     [("Zergatik zatoz berandu?", "¿Por qué vienes tarde?"), ("Autobusa galdu dudalako.", "Porque he perdido el autobús."), ("Zergatik zaude triste?", "¿Por qué estás triste?"), ("Nekatuta nagoelako.", "Porque estoy cansado.")]),
    42: ("nahiz-eta-arren", "Aunque: nahiz eta", "cómo decir aunque", [
        ("Nahiz eta euria egin, kalera noa.", "Aunque llueva, salgo a la calle.", "Aunque se dice nahiz eta, y el verbo va sin terminación."),
        ("Nahiz eta gaixorik egon, lanera joan da.", "Aunque está enfermo, ha ido a trabajar."), ("Garestia bada ere, erosiko dut.", "Aunque sea caro, lo compraré.", "Otra forma es poner ba delante del verbo y ere detrás."),
        ("Euria ari badu ere, ateratzen naiz.", "Aunque llueva, salgo."), ("Zaharra izan arren, indartsua da.", "A pesar de ser mayor, es fuerte.", "Y a pesar de se dice arren."), ("Ondo ikasi arren, ez dut gogoratzen.", "A pesar de estudiar bien, no lo recuerdo."),
        ("Hala ere, etorri da.", "Aun así, ha venido."), ("Hala ere, pozik nago.", "Aun así, estoy contento.")],
     [("Kalera zoaz?", "¿Sales a la calle?"), ("Bai, nahiz eta euria egin.", "Sí, aunque llueva."), ("Nekatuta zaude?", "¿Estás cansado?"), ("Bai, baina hala ere noa.", "Sí, pero aun así voy.")]),
    43: ("eman-diot", "Dar algo a alguien", "dar algo a alguien", [
        ("Aitonari ogia eman diot.", "Le he dado el pan al abuelo.", "Cuando hay alguien que recibe, el verbo cambia. Le he dado, se dice diot."),
        ("Amak gutun bat idatzi dit.", "La madre me ha escrito una carta.", "Me lo ha dado, dit."), ("Zuri opari bat ekarri dizut.", "Te he traído un regalo.", "Te lo he dado, dizut."), ("Niri dirua eman didazu.", "Me has dado dinero."),
        ("Aitari esan diogu.", "Se lo hemos dicho al padre."), ("Lagunei idatzi diet.", "Les he escrito a los amigos."), ("Zer esan dizu?", "¿Qué te ha dicho?"), ("Egia esan dit.", "Me ha dicho la verdad.")],
     [("Zer esan dizu aitonak?", "¿Qué te ha dicho el abuelo?"), ("Egia esan dit.", "Me ha dicho la verdad."), ("Eta zuk zer eman diozu?", "¿Y tú qué le has dado?"), ("Opari bat eman diot.", "Le he dado un regalo.")]),
    45: ("trenez-eta-euskaraz", "En tren, a mano, en euskera", "cómo decir en tren o en euskera", [
        ("Trenez noa Bilbora.", "Voy a Bilbao en tren.", "Para decir con qué medio se hace algo, se añade z o ez."),
        ("Autobusez joan gara.", "Hemos ido en autobús."), ("Oinez etorri naiz.", "He venido a pie."), ("Hegazkinez joango gara.", "Iremos en avión."),
        ("Euskaraz hitz egiten dut.", "Hablo en euskera."), ("Eskuz idatzi dut.", "Lo he escrito a mano."), ("Zertaz ari zara?", "¿De qué estás hablando?", "De qué tema se habla también se dice con z."), ("Politikaz hitz egiten ari gara.", "Estamos hablando de política.")],
     [("Nola etorri zara?", "¿Cómo has venido?"), ("Trenez etorri naiz. Eta zu?", "He venido en tren. ¿Y tú?"), ("Ni oinez etorri naiz.", "Yo he venido a pie."), ("Euskaraz hitz egingo dugu?", "¿Hablamos en euskera?")]),
    46: ("ikastea-zaila-da", "Leer es bueno: hablar de acciones", "cómo hablar de las acciones", [
        ("Paseatzea gustatzen zait.", "Me gusta pasear.", "Para hablar de una acción como si fuera una cosa, el verbo termina en tzea o tea."),
        ("Irakurtzea ona da.", "Leer es bueno."), ("Euskara ikastea zaila da.", "Aprender euskera es difícil."), ("Goiz jaikitzea ez zait gustatzen.", "No me gusta levantarme temprano."),
        ("Erretzea txarra da osasunerako.", "Fumar es malo para la salud."), ("Hau egitea erraza da.", "Hacer esto es fácil."), ("Ikasteko gogoa daukat.", "Tengo ganas de aprender."), ("Amonari kantatzea gustatzen zaio.", "A la abuela le gusta cantar.")],
     [("Zer gustatzen zaizu?", "¿Qué te gusta?"), ("Paseatzea eta irakurtzea.", "Pasear y leer."), ("Euskara ikastea zaila da?", "¿Es difícil aprender euskera?"), ("Bai, baina ikasteko gogoa daukat.", "Sí, pero tengo ganas de aprender.")]),
    # ---------------- B1 ----------------
    48: ("euskaldunok-eta-biok", "Nosotros los vascos, y tú y yo", "cómo decir nosotros los vascos", [
        ("Euskaldunok pilota maite dugu.", "A los vascos nos encanta la pelota.", "Si tú formas parte del grupo, el nombre termina en ok, y no en ak."),
        ("Aitonok asko dakigu.", "Los abuelos sabemos mucho."), ("Emakumeok lanean ari gara.", "Las mujeres estamos trabajando."),
        ("Zu eta biok joango gara.", "Iremos tú y yo.", "Tú y yo juntos se dice zu eta biok."), ("Aita eta biok etxean geratu gara.", "Mi padre y yo nos hemos quedado en casa."),
        ("Haurrak etorri dira.", "Los niños han venido.", "Fíjate en la diferencia. Con verbos como venir, el nombre termina en ak."), ("Haurrek ogia jan dute.", "Los niños han comido pan.", "Y con verbos como comer, el nombre termina en ek."), ("Gizonek lan egin dute.", "Los hombres han trabajado.")],
     [("Norekin joango zara?", "¿Con quién irás?"), ("Zu eta biok joango gara.", "Iremos tú y yo."), ("Eta aitonak?", "¿Y los abuelos?"), ("Aitonok etxean geratuko gara.", "Los abuelos nos quedaremos en casa.")]),
    49: ("galdegaia", "Lo importante va delante del verbo", "el orden de la frase", [
        ("Nor etorri da?", "¿Quién ha venido?", "En euskera, lo más importante de la frase va justo delante del verbo."),
        ("Mikel etorri da.", "Ha venido Mikel."), ("Noiz joan zinen Bilbora?", "¿Cuándo fuiste a Bilbao?"), ("Atzo joan nintzen Bilbora.", "Fui a Bilbao ayer."),
        ("Nora joan zinen atzo?", "¿A dónde fuiste ayer?"), ("Bilbora joan nintzen atzo.", "Ayer fui a Bilbao."), ("Nik egin dut.", "Lo he hecho yo."), ("Etorri egin da.", "Sí que ha venido.", "Para resaltar la acción, se repite con el verbo egin.")],
     [("Nork egin du hau?", "¿Quién ha hecho esto?"), ("Nik egin dut.", "Lo he hecho yo."), ("Noiz egin duzu?", "¿Cuándo lo has hecho?"), ("Gaur egin dut.", "Lo he hecho hoy.")]),
    50: ("neska-eta-eliza", "Las palabras que ya terminan en a", "las palabras que ya terminan en a", [
        ("Neska etorri da.", "La chica ha venido.", "Algunas palabras terminan en a de por sí, como neska. No se le añade otra."),
        ("Hiru neska etorri dira.", "Han venido tres chicas."), ("Neskek kantatu dute.", "Las chicas han cantado.", "En plural esa a desaparece, y queda ek."), ("Hau eliza da.", "Esto es una iglesia."),
        ("Elizan nago.", "Estoy en la iglesia."), ("Eskolara noa.", "Voy a la escuela."), ("Eskolatik nator.", "Vengo de la escuela."), ("Denda batean erosi dut.", "Lo he comprado en una tienda.")],
     [("Non dago neska?", "¿Dónde está la chica?"), ("Eskolara joan da.", "Ha ido a la escuela."), ("Eta mutilak?", "¿Y los chicos?"), ("Elizan daude.", "Están en la iglesia.")]),
    51: ("etor-naiteke", "Poder hacer algo: etor naiteke", "otra forma de decir que puedes", [
        ("Etor naiteke.", "Puedo venir.", "Hay una forma más cuidada de decir puedo, con verbos especiales como naiteke."),
        ("Etor zaitezke?", "¿Puedes venir?"), ("Joan daiteke.", "Puede ir."), ("Hemen eser zaitezke.", "Puedes sentarte aquí."), ("Ezin naiz joan.", "No puedo ir."),
        ("Ikus dezaket.", "Puedo verlo.", "Con verbos como ver se dice dezaket."), ("Egin dezakezu?", "¿Puedes hacerlo?"), ("Esan diezazuket.", "Te lo puedo decir.", "Y si hay alguien que recibe, diezazuket.")],
     [("Etor zaitezke bihar?", "¿Puedes venir mañana?"), ("Ez, ezin naiz joan.", "No, no puedo ir."), ("Lagundu dezakezu?", "¿Puedes ayudar?"), ("Bai, egin dezaket.", "Sí, puedo hacerlo.")]),
    53: ("baino-lehen-ondoren", "Antes, mientras y después", "cómo decir antes y después", [
        ("Etxera iritsi baino lehen, ogia erosi dut.", "Antes de llegar a casa, he comprado el pan.", "Antes de se dice baino lehen."),
        ("Lo egin aurretik, irakurtzen dut.", "Antes de dormir, leo."), ("Afaltzen dugun bitartean, irratia entzuten dugu.", "Mientras cenamos, escuchamos la radio.", "Mientras se dice bitartean."),
        ("Bazkaldu ondoren, ibiltzen naiz.", "Después de comer, ando.", "Después se dice ondoren."), ("Jaiki eta berehala, kafea hartzen dut.", "Nada más levantarme, tomo café."),
        ("Etorri bezain laster, deituko dizut.", "En cuanto venga, te llamaré."), ("Ikusten dudanean, esango diot.", "Cuando lo vea, se lo diré."), ("Gaztetan asko lan egiten nuen.", "De joven trabajaba mucho.")],
     [("Noiz deituko didazu?", "¿Cuándo me llamarás?"), ("Etorri bezain laster.", "En cuanto venga."), ("Eta bazkaldu aurretik?", "¿Y antes de comer?"), ("Bazkaldu ondoren hobeto.", "Mejor después de comer.")]),
    54: ("noraino-eta-bera", "Hasta dónde, y el mismo", "hasta dónde llegamos", [
        ("Noraino zoaz?", "¿Hasta dónde vas?", "Hasta un lugar se dice añadiendo raino."),
        ("Bilboraino noa.", "Voy hasta Bilbao."), ("Etxeraino lagunduko zaitut.", "Te acompañaré hasta casa."), ("Hondartzaraino oinez joan gara.", "Hemos ido a pie hasta la playa."),
        ("Hamargarren orrialderaino irakurri dut.", "He leído hasta la página diez."), ("Gizon bera da.", "Es el mismo hombre.", "El mismo se dice bera, detrás del nombre."), ("Etxe bera da.", "Es la misma casa."),
        ("Zure autoa nirearen berdina da.", "Tu coche es igual que el mío.", "Igual se dice berdina.")],
     [("Noraino zoaz?", "¿Hasta dónde vas?"), ("Hondartzaraino noa.", "Voy hasta la playa."), ("Etxeraino lagunduko zaitut.", "Te acompañaré hasta casa."), ("Eskerrik asko.", "Muchas gracias.")]),
    55: ("ez-dakit-non-dagoen", "No sé dónde está", "cómo decir no sé dónde está", [
        ("Ez dakit non dagoen.", "No sé dónde está.", "Cuando una pregunta va dentro de otra frase, el verbo termina en n."),
        ("Galdetu dit nor zaren.", "Me ha preguntado quién eres."), ("Badakizu noiz etorriko den?", "¿Sabes cuándo vendrá?"), ("Esan iezadazu zer egin duzun.", "Dime qué has hecho."),
        ("Agian etorriko da.", "Quizá venga."), ("Beharbada bihar joango gara.", "Tal vez vayamos mañana."), ("Seguru asko euria egingo du.", "Seguramente lloverá."), ("Noski, lagunduko dizut.", "Claro, te ayudaré.")],
     [("Badakizu non dagoen aitona?", "¿Sabes dónde está el abuelo?"), ("Ez dakit non dagoen.", "No sé dónde está."), ("Etorriko da?", "¿Vendrá?"), ("Seguru asko etorriko da.", "Seguramente vendrá.")]),
    57: ("etor-dadila", "Mandar con cuidado: que venga", "cómo decir que venga", [
        ("Etor dadila.", "Que venga.", "Para decir que venga alguien, se usa dadila."),
        ("Joan daitezela.", "Que se vayan."), ("Har dezala.", "Que lo coja."), ("Goazen!", "¡Vamos!", "Para animar a todos, se dice goazen."), ("Egin dezagun.", "Hagámoslo."),
        ("Esadazu egia.", "Dime la verdad."), ("Emaiozu ogia aitonari.", "Dale el pan al abuelo."), ("Ez ezazu hori esan.", "No digas eso.")],
     [("Non dago Mikel?", "¿Dónde está Mikel?"), ("Etor dadila hona.", "Que venga aquí."), ("Goazen etxera!", "¡Vamos a casa!"), ("Esadazu egia, nekatuta zaude?", "Dime la verdad, ¿estás cansado?")]),
    58: ("exklamazioak-eta-datak", "Exclamar y decir la fecha", "exclamaciones y fechas", [
        ("Zeinen polita!", "¡Qué bonito!", "Para exclamar se puede empezar con zeinen."), ("A zer eguna!", "¡Vaya día!"), ("Hau da hotza!", "¡Vaya frío!"),
        ("Zein egun da gaur?", "¿Qué día es hoy?"), ("Gaur azaroaren bederatzia da.", "Hoy es nueve de noviembre.", "En la fecha se dice primero el mes y luego el día."),
        ("Noiz da zure urtebetetzea?", "¿Cuándo es tu cumpleaños?"), ("Maiatzaren hamarrean jaio nintzen.", "Nací el diez de mayo."), ("Mila bederatziehun eta berrogeita hamarrean jaio nintzen.", "Nací en mil novecientos cincuenta.")],
     [("Noiz jaio zinen, aitona?", "¿Cuándo naciste, abuelo?"), ("Maiatzaren hamarrean jaio nintzen.", "Nací el diez de mayo."), ("Zein egun da gaur?", "¿Qué día es hoy?"), ("A zer eguna! Hau da hotza!", "¡Vaya día! ¡Vaya frío!")]),
    59: ("bai-bai-ez-ez", "Tanto uno como otro", "cómo unir ideas", [
        ("Ez dut kafea nahi, ezta tea ere.", "No quiero café, ni té tampoco.", "Ni se dice ezta, y detrás va ere."),
        ("Bai Mikel, bai Amaia etorri dira.", "Han venido tanto Mikel como Amaia.", "Tanto uno como otro se dice repitiendo bai."), ("Hala aita, nola ama, pozik daude.", "Tanto el padre como la madre están contentos."),
        ("Euria dela, eguzkia dela, ateratzen naiz.", "Llueva o haga sol, salgo.", "Sea esto o aquello se dice dela, dela."), ("Gazteak ez ezik, zaharrak ere etorri dira.", "No solo los jóvenes, también han venido los mayores.", "No solo se dice ez ezik."),
        ("Zein kafea, zein tea, biak gustatzen zaizkit.", "Tanto el café como el té, me gustan los dos."), ("Ez naiz joan, ezta zu ere.", "No he ido, ni tú tampoco."), ("Hau ez ezik, hori ere nahi dut.", "No solo esto, también quiero eso.")],
     [("Kafea edo tea?", "¿Café o té?"), ("Bai bata, bai bestea.", "Tanto uno como otro."), ("Kalera zoaz euria ari badu?", "¿Sales si llueve?"), ("Euria dela, eguzkia dela, ateratzen naiz.", "Llueva o haga sol, salgo.")]),
    61: ("asko-eta-handia", "Mucho y grande: asko y handia", "cómo decir mucho", [
        ("Jende asko dago.", "Hay mucha gente.", "Mucho se dice asko, cuando se cuenta."), ("Diru asko daukat.", "Tengo mucho dinero."),
        ("Bero handia egiten du.", "Hace mucho calor.", "Pero con calor, frío o miedo se usa handia."), ("Hotz handia egiten du.", "Hace mucho frío."), ("Beldur handia izan dut.", "He tenido mucho miedo."),
        ("Etorri naiz zu ikusi nahi zaitudalako.", "He venido porque quiero verte."), ("Ez dut erosi garestiegia delako.", "No lo he comprado porque es demasiado caro."), ("Pozik nago, oporretan nagoelako.", "Estoy contento porque estoy de vacaciones.")],
     [("Bero handia egiten du.", "Hace mucho calor."), ("Bai, eta jende asko dago.", "Sí, y hay mucha gente."), ("Zergatik zaude pozik?", "¿Por qué estás contento?"), ("Oporretan nagoelako.", "Porque estoy de vacaciones.")]),
    62: ("zuregan-bigarren", "Pensar en ti, y el segundo", "pensar en alguien, y contar en orden", [
        ("Zuregan pentsatzen dut.", "Pienso en ti.", "En una persona se dice con gan. En mí, niregan, y en ti, zuregan."), ("Aitarengan pentsatzen dut.", "Pienso en mi padre."),
        ("Zuregan sinesten dut.", "Creo en ti."), ("Lagunengan konfiantza daukat.", "Tengo confianza en los amigos."), ("Lehenengo etxea hau da.", "La primera casa es esta.", "El orden se dice añadiendo garren."),
        ("Bigarren etxea zurea da.", "La segunda casa es tuya."), ("Hirugarren solairuan bizi naiz.", "Vivo en el tercer piso."), ("Laugarren aldia da.", "Es la cuarta vez.")],
     [("Zertan pentsatzen ari zara?", "¿En qué estás pensando?"), ("Zuregan pentsatzen ari naiz.", "Estoy pensando en ti."), ("Non bizi zara?", "¿Dónde vives?"), ("Hirugarren solairuan bizi naiz.", "Vivo en el tercer piso.")]),
    63: ("euria-ari-badu", "Si llueve: el condicional real", "cómo decir si", [
        ("Euria ari badu, etxean geratuko naiz.", "Si llueve, me quedaré en casa.", "Si se dice poniendo ba delante del verbo."),
        ("Etortzen bazara, pozik egongo naiz.", "Si vienes, estaré contento."), ("Dirua badaukat, erosiko dut.", "Si tengo dinero, lo compraré."), ("Nahi baduzu, lagunduko dizut.", "Si quieres, te ayudaré."),
        ("Gose bazara, jan.", "Si tienes hambre, come."), ("Gaixorik bazaude, joan medikuarengana.", "Si estás enfermo, ve al médico."), ("Ez bazatoz, deitu.", "Si no vienes, llama."), ("Ondo ikasten baduzu, ulertuko duzu.", "Si estudias bien, lo entenderás.")],
     [("Bihar etorriko zara?", "¿Vendrás mañana?"), ("Euria ari badu, ez.", "Si llueve, no."), ("Nahi baduzu, lagunduko dizut.", "Si quieres, te ayudaré."), ("Eskerrik asko.", "Muchas gracias.")]),
    # ---------------- B2 ----------------
    65: ("aberatsa-banintz", "Si fuera rico: lo imaginario", "lo que harías si pudieras", [
        ("Aberatsa banintz, etxe bat erosiko nuke.", "Si fuera rico, compraría una casa.", "Para lo que solo imaginamos, soy se convierte en banintz, y al final se dice nuke."),
        ("Gazteago banintz, mendira joango nintzateke.", "Si fuera más joven, iría al monte."), ("Etorriko balitz, pozik egongo nintzateke.", "Si viniera, estaría contento."), ("Hemen bazina, lagunduko zenidake.", "Si estuvieras aquí, me ayudarías."),
        ("Joango banintz, abisatuko nizuke.", "Si fuera, te avisaría."), ("Atzo etorri izan bazina, ikusiko ninduzun.", "Si hubieras venido ayer, me habrías visto."), ("Mikel izan ezik, denak etorri dira.", "Excepto Mikel, han venido todos.", "Excepto se dice izan ezik."), ("Bera ez ezik, ni ere banoa.", "No solo él, también voy yo.")],
     [("Zer egingo zenuke aberatsa bazina?", "¿Qué harías si fueras rico?"), ("Etxe bat erosiko nuke.", "Compraría una casa."), ("Non?", "¿Dónde?"), ("Gazteago banintz, mendian.", "Si fuera más joven, en el monte.")]),
    66: ("baneki-esango-nizuke", "Si lo supiera, te lo diría", "más sobre lo imaginario", [
        ("Baneki, esango nizuke.", "Si lo supiera, te lo diría.", "Con verbos como saber se dice baneki."), ("Diru gehiago banu, bidaiatuko nuke.", "Si tuviera más dinero, viajaría."), ("Ikusiko banu, agurtuko nuke.", "Si lo viera, lo saludaría."),
        ("Gustatuko balitzait, erosiko nuke.", "Si me gustara, lo compraría.", "Si le pasa algo a alguien, se dice balitzait."), ("Ahaztuko balitzaizu, deituko nizuke.", "Si se te olvidara, te llamaría."),
        ("Ekarriko bazenit, eskertuko nizuke.", "Si me lo trajeras, te lo agradecería."), ("Esango bazenio, pozik egongo litzateke.", "Si se lo dijeras, estaría contento."), ("Emango banio, haserretuko litzateke.", "Si se lo diera, se enfadaría.")],
     [("Badakizu non dagoen?", "¿Sabes dónde está?"), ("Baneki, esango nizuke.", "Si lo supiera, te lo diría."), ("Gustatuko litzaizuke?", "¿Te gustaría?"), ("Diru gehiago banu, bai.", "Si tuviera más dinero, sí.")]),
    67: ("omen-ote-bezala", "Dicen que, ¿será que?, y como", "cómo contar lo que se dice", [
        ("Etorri omen da.", "Dicen que ha venido.", "La palabra omen indica que lo sabes por otros."), ("Aberatsa omen da.", "Dicen que es rico."),
        ("Non ote dago?", "¿Dónde estará?", "La palabra ote expresa duda."), ("Etorriko ote da?", "¿Vendrá?"), ("Laguntzat hartzen zaitut.", "Te considero un amigo.", "Tomar a alguien por algo se dice con tzat."),
        ("Ergeltzat hartu nau.", "Me ha tomado por tonto."), ("Nik esan bezala egin dut.", "Lo he hecho como yo he dicho.", "Como se dice bezala."), ("Zu bezalako lagunak behar ditut.", "Necesito amigos como tú.")],
     [("Mikel etorri omen da.", "Dicen que ha venido Mikel."), ("Non ote dago?", "¿Dónde estará?"), ("Ez dakit.", "No lo sé."), ("Zu bezalako lagunak behar ditut.", "Necesito amigos como tú.")]),
    69: ("batere-samar-izugarri", "Nada, bastante, muchísimo", "cómo graduar lo que dices", [
        ("Ez dut batere gogorik.", "No tengo nada de ganas.", "Nada en absoluto se dice batere."), ("Batere ez zait gustatzen.", "No me gusta nada."),
        ("Nekatuta samar nago.", "Estoy bastante cansado.", "Un poco se dice samar, y va detrás."), ("Nahiko ondo nago.", "Estoy bastante bien."), ("Polit samarra da.", "Es bastante bonito."),
        ("Izugarri gustatzen zait.", "Me gusta muchísimo.", "Muchísimo se dice izugarri."), ("Ikaragarri hotz egiten du.", "Hace un frío tremendo."), ("Erdi lo nago.", "Estoy medio dormido.")],
     [("Zer moduz zaude?", "¿Cómo estás?"), ("Nekatuta samar nago.", "Estoy bastante cansado."), ("Kalera goaz?", "¿Salimos?"), ("Ez, ez dut batere gogorik.", "No, no tengo nada de ganas.")]),
    70: ("neu-zuregatik", "Yo mismo, y por ti", "yo mismo, y por quién hacemos las cosas", [
        ("Neu joango naiz.", "Iré yo mismo.", "Para reforzar, ni se convierte en neu. Y zu, en zeu."), ("Zeuk egin duzu.", "Lo has hecho tú mismo."), ("Geuk ordainduko dugu.", "Lo pagaremos nosotros mismos."), ("Berak esan dit.", "Me lo ha dicho él."),
        ("Zuregatik etorri naiz.", "He venido por ti.", "Por alguien se dice gatik."), ("Aitarengatik egin dut.", "Lo he hecho por mi padre."), ("Haurrengatik lan egiten dut.", "Trabajo por los niños."), ("Ez da diruagatik.", "No es por el dinero.")],
     [("Nork egin du?", "¿Quién lo ha hecho?"), ("Neuk egin dut.", "Lo he hecho yo mismo."), ("Zergatik?", "¿Por qué?"), ("Zuregatik egin dut.", "Lo he hecho por ti.")]),
    71: ("norantz-eta-arazi", "Hacia dónde, y hacer que alguien haga", "hacia dónde y hacer hacer", [
        ("Norantz zoaz?", "¿Hacia dónde vas?", "Hacia un lugar se dice rantz."), ("Etxerantz noa.", "Voy hacia casa."), ("Itsasorantz begiratu dut.", "He mirado hacia el mar."), ("Mendirantz joan gara.", "Hemos ido hacia el monte."),
        ("Amak janarazi dit.", "La madre me ha hecho comer.", "Hacer que alguien haga algo se dice arazi."), ("Medikuak ibilarazi nau.", "El médico me ha hecho andar."), ("Irakasleak idatzarazi digu.", "El profesor nos ha hecho escribir."), ("Etxea konponarazi dut.", "He mandado arreglar la casa.")],
     [("Norantz zoaz?", "¿Hacia dónde vas?"), ("Mendirantz noa.", "Voy hacia el monte."), ("Zergatik?", "¿Por qué?"), ("Medikuak ibilarazi nau.", "El médico me ha hecho andar.")]),
    73: ("zertarako-edozer", "Para qué, y cualquier cosa", "para qué hacemos las cosas", [
        ("Zertarako etorri zara?", "¿Para qué has venido?", "Para qué se dice zertarako."), ("Ikasteko etorri naiz.", "He venido para aprender.", "Para hacer algo, el verbo termina en teko o tzeko."), ("Ogia erosteko dirua behar dut.", "Necesito dinero para comprar pan."),
        ("Edonor etor daiteke.", "Puede venir cualquiera.", "Cualquiera se dice edonor."), ("Edozer jango dut.", "Comeré cualquier cosa."), ("Edonon lo egiten dut.", "Duermo en cualquier sitio."),
        ("Bilborako trena da.", "Es el tren para Bilbao.", "Hacia un destino se dice rako."), ("Bihar goizerako prest egongo da.", "Estará listo para mañana por la mañana.")],
     [("Zertarako behar duzu dirua?", "¿Para qué necesitas dinero?"), ("Ogia erosteko.", "Para comprar pan."), ("Zer jango duzu?", "¿Qué comerás?"), ("Edozer jango dut.", "Comeré cualquier cosa.")]),
    74: ("dakidanez-zenbateko", "Según sé, y de qué tamaño", "según lo que sé", [
        ("Dakidanez, ez da etorri.", "Según sé, no ha venido.", "Según se dice añadiendo nez al verbo."), ("Esan dutenez, euria egingo du.", "Según han dicho, lloverá."), ("Entzun dudanez, oso ona da.", "Según he oído, es muy bueno."),
        ("Ikusten dudanez, ondo zaude.", "Según veo, estás bien."), ("Zu ikusteko etorri naiz.", "He venido para verte."), ("Ondo ikasteko, egunero entzun.", "Para aprender bien, escucha todos los días."),
        ("Zenbateko etxea da?", "¿De qué tamaño es la casa?", "De qué tamaño o cuánto se dice zenbateko."), ("Zenbateko gizona!", "¡Qué hombretón!")],
     [("Etorri da Mikel?", "¿Ha venido Mikel?"), ("Dakidanez, ez da etorri.", "Según sé, no ha venido."), ("Eta bihar?", "¿Y mañana?"), ("Esan dutenez, euria egingo du.", "Según han dicho, lloverá.")]),
    75: ("bezain-eta-beste", "Tan como y tanto como", "tan alto como tú", [
        ("Zu bezain altua naiz.", "Soy tan alto como tú.", "Tan como se dice bezain."), ("Aita bezain gizon ona da.", "Es tan buen hombre como su padre."), ("Hau hori bezain garestia da.", "Esto es tan caro como eso."),
        ("Nahi duzun beste jan.", "Come tanto como quieras.", "Tanto como se dice beste."), ("Ahal duzun beste lagundu.", "Ayuda tanto como puedas."), ("Nik beste daki.", "Sabe tanto como yo."),
        ("Labanaz moztu dut.", "Lo he cortado con un cuchillo.", "Con una cosa se dice con z, y con una persona, con rekin."), ("Aitarekin moztu dut.", "Lo he cortado con mi padre.")],
     [("Nor da altuena?", "¿Quién es el más alto?"), ("Zu bezain altua naiz.", "Soy tan alto como tú."), ("Jan nahi duzu?", "¿Quieres comer?"), ("Bai, nahi dudan beste.", "Sí, tanto como quiera.")]),
    77: ("deritzot-buruz-bina", "Opinar, hablar sobre, y de dos en dos", "dar una opinión", [
        ("Zer deritzozu?", "¿Qué te parece?", "Para opinar se usa un verbo especial, deritzot."), ("Ona deritzot.", "Me parece bueno."), ("Zer deritzozu liburu honi?", "¿Qué te parece este libro?"),
        ("Zuri buruz hitz egin dugu.", "Hemos hablado sobre ti.", "Sobre se dice buruz."), ("Euskarari buruzko liburua da.", "Es un libro sobre el euskera."), ("Mendiari buruz asko daki.", "Sabe mucho sobre el monte."),
        ("Bina sagar hartu ditugu.", "Hemos cogido dos manzanas cada uno.", "De dos en dos se dice bina, y de tres en tres hiruna."), ("Hiruna euro ordaindu dugu.", "Hemos pagado tres euros cada uno.")],
     [("Zer deritzozu liburu honi?", "¿Qué te parece este libro?"), ("Ona deritzot.", "Me parece bueno."), ("Zeri buruz da?", "¿Sobre qué es?"), ("Euskarari buruzko liburua da.", "Es un libro sobre el euskera.")]),
    78: ("gero-eta-hobeto", "Cada vez mejor", "cada vez mejor", [
        ("Ahalik eta azkarren etorri.", "Ven lo más rápido posible.", "Lo más posible se dice ahalik eta, y el adjetivo termina en en."), ("Ahalik eta ondoen egingo dut.", "Lo haré lo mejor posible."),
        ("Gero eta hobeto nago.", "Estoy cada vez mejor.", "Cada vez más se dice gero eta."), ("Gero eta zaharragoa naiz.", "Cada vez soy más mayor."), ("Gero eta euskara gehiago dakit.", "Cada vez sé más euskera."),
        ("Zenbat eta gehiago ikasi, orduan eta gehiago jakin.", "Cuanto más se estudia, más se sabe.", "Cuanto más, más, se dice zenbat eta, orduan eta."), ("Zenbat eta lehenago, orduan eta hobe.", "Cuanto antes, mejor."), ("Gero eta hotzago dago.", "Hace cada vez más frío.")],
     [("Zer moduz euskara, aitona?", "¿Qué tal el euskera, abuelo?"), ("Gero eta hobeto.", "Cada vez mejor."), ("Asko dakizu!", "¡Sabes mucho!"), ("Zenbat eta gehiago ikasi, orduan eta gehiago jakin.", "Cuanto más se estudia, más se sabe.")]),
    79: ("azentua-eta-hatxea", "El acento vasco y la hache", "cómo se pronuncia bien", [
        ("Euskal Herria.", "El País Vasco.", "Hoy cuidamos la pronunciación. En euskera, las sílabas suenan parejas, sin golpes fuertes como en castellano."),
        ("Hitz bat esan.", "Di una palabra.", "La hache se escribe, pero aquí casi nunca suena."), ("Haurrak hondartzan daude.", "Los niños están en la playa."), ("Herri honetan bizi naiz.", "Vivo en este pueblo."),
        ("Ohean nago.", "Estoy en la cama."), ("Ez ahaztu.", "No lo olvides."), ("Eta abar.", "Etcétera."), ("Euskara ondo ahoskatzen dut.", "Pronuncio bien el euskera.")],
     [("Non daude haurrak?", "¿Dónde están los niños?"), ("Hondartzan daude.", "Están en la playa."), ("Ez ahaztu!", "¡No lo olvides!"), ("Agur, aitona. Eskerrik asko.", "Adiós, abuelo. Muchas gracias.")]),
}

# n: (de que episodios repasa)
REPASOS = {
    28: [25, 26, 27], 32: [29, 30, 31], 36: [33, 34, 35], 40: [37, 38, 39], 44: [41, 42, 43], 47: [45, 46],
    52: [48, 49, 50, 51], 56: [53, 54, 55], 60: [57, 58, 59], 64: [61, 62, 63],
    68: [65, 66, 67], 72: [69, 70, 71], 76: [73, 74, 75], 80: [77, 78, 79],
}

SIGUIENTE_A1 = {22: "cuánto vale algo y qué quieres", 24: "lo que estás haciendo ahora"}

NIVELES = (("A1", 1, 24), ("A2", 25, 47), ("B1", 48, 64), ("B2", 65, 80))


def nivel_de(n):
    return next(nombre for nombre, de, a in NIVELES if de <= n <= a)


def normaliza(item):
    return (item[0], item[1], [("ES", item[2])] if len(item) > 2 else None)


def ampliar(episodios):
    """Anade a EPISODIOS lo de este archivo."""
    for n, extra in A1_AMPLIAR.items():
        episodios[n]["items"] += [normaliza(i) for i in extra]
    for n, s in SIGUIENTE_A1.items():
        episodios[n]["siguiente"] = s
    numeros = sorted(set(NUEVOS) | set(REPASOS))
    for n, (slug, titulo, _, items, dialogo) in NUEVOS.items():
        episodios[n] = dict(slug=slug, titulo=titulo, items=[normaliza(i) for i in items], dialogo=dialogo)
    for n, de in REPASOS.items():
        episodios[n] = dict(slug=f"errepasoa-{n}", titulo="Repaso", repaso=True, de=de)
    for i, n in enumerate(numeros):
        siguiente = next((k for k in numeros[i + 1:] if k in NUEVOS), None)
        episodios[n]["siguiente"] = NUEVOS[siguiente][2] if siguiente else None
