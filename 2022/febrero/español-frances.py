dict1={"Baloncesto":"Le basket",
      "Futbol Americano":"Le football américain"
      "Voleibol de Playa":"Le beach-volley"
      "Futbol":"Le football"
      "Hockey sobre Hierba":"Le hockey sur gazon"
      "BalonMano":"Le handball"
      "Golf":"Le golf"
      "Voleibol":"Le volley-ball"
      "Rugby":"Le rugby"
      "Taekwondo":"Le taekwondo"
      "Judo":"Le judo"
      "Karate":"Le karaté"
      "Badminton":"Le badminton"
      "Tenis de mesa":"Le tennis de table"
      "Tenis":"Le tennis"
      "Remo":"L’aviron"
      "Salto de Trampolin":"Le plongeon"
      "Natacion":"La natation"
      "Vela":"La voile"
      "Waterpolo":"Le waterpolo"
      "Natación sincronizada o nado sincronizado":"La natation synchronisée"
      "Boxeo":"La boxe"
      "Tiro con Arco":"Le tir à l’arc"
      "Ajedrez":"Les échecs"
      "Ciclismo":"Le cyclisme"
      "Esgrima":"L’escrime"
      "Equitacion":"L’équitation"
      "Tiro Deportivo ":"Le tir sportif"
      "Gimnasia":"La gymnastique"
      "Lucha":"La lutte"
      "Halterofilia o levantamiento de pesas":"L’haltérophilie"
      "Triatlon":"Le triathlon"
      "Acrobacia":"acrobaties"
      "Ejercicio aeróbico":"Exercice d'aérobie"
      "Aikido":"Aïkido"
      "Atletismo":"athlétisme"
      "Beisbol":"base-ball"
      "Billar":"Billard"
      "Culturismo":"La Musculation"
      "Bolos":"Bowling"
      "Saltar al Vacio":"sauter dans le vide"
      "Regata":"Course"
      "Piraguismo":"canoë-kayak"
      "Entrenamiento cardiovascular":"exercices d'entraînement cardiovasculaires"
      "Automovilismo":"l'automobile"
      "Criquet":"Criquet"
      "CicloCross":"cyclocross, course cycliste sur terrain"
      "Curling":"Curling"
      "Dardos":"fléchettes"
      "Buceo":"plongée"
      "Pesca":"faire de la pêche"
      "fútbol sala":"foot en salle"
      " karting":"je vais faire du kart"
      "Ala Delta":"aile delta"
      "Senderismo":"randonnée"
      "Caza":"chasse"
      "hockey sobre hielo":"hockey sur glace"
      "Kickboxing":"kick-boxing"
      "Kung Fu":"Kung Fu"
      "Salto de longitud":"saut en longueur"
      "Artes Marciales":"arts martiaux"
      "Maraton":"marathon"
      "Motonáutica":"bateau à moteur"
      "Motociclismo":"faire de la moto"
      "Alpinismo":"Alpinisme"
      "Paint Ball":"Paint-ball"
      "Padel":"Pagayer"
      "ParaCaidismo":"Parachustime"
      "Parapente":"Parapente"
      "Parkour":"Parkour"
      "Salto con Pertiga":"Saut à la perche"
      "Raquetbol":"Racquetball"
      "Canotaje":"Rafting"
      "Descenso con Cuerda":"Descente de corde"
      "Gimnasia rítmica":"Gymnastique rythmique"
      "Anillas":"Anneaux"
      "Escalada":"Escalade"
      "Hockey Sobre Patines":"Hockey à roulettes"
      "Saltar La Cuerda":"Sauter à la corde"
      "Correr":"Courir"
      "Buceo":"Plongée"
      "Patinaje":"Patinage"
      "SkateBoard":"Faire de la planche à roulettes"
      "Esqui":"Ski"
      "Esnorquel":"Tuba"
      "SnowBoard":"Planche a neige"
      "SoftBol":"Baile Molle"
      "Squash":"écraser"
      "Estiramiento":"élongation"
      "Sumo":"Sumo"
      "Surf":"Le Surf"
      "Trapecio":"trapèze"
      "Deportes Acuaticos":"Sports aquatiques"
      "Levantamiento de pesas, halterofilia"
      "Waterpolo":"Water Polo"
      "Windsurf":"planche à voile"
      "Esquí acuático":"Ski nautique"
      "Deportes de Invierno":"Sports d'hiver"}

def search_word(dict):
    word=input("ingrese la palabra que desea traducir: ")
    for p in dict.keys():
        if word==p:
            print("la traduccion de la palabra",word"al frances es: ",dict[p])
            return None

print(search_word(dict1))

