label gk320:
    call hide_menu
    "------------scene 320 Metarivali part 1-------------"

    scene black onlayer underlayer
    scene witch_flowers
    with purple_flash
    play music "audio/umi/black liliana.mp3" #oppure scorpion entrails
    play sound "audio/sfx/teleport.wav"
    show check sor fp think worried at left
    show check at flip
    show hnb yepper close at right
    with squares

    "Esce dalla esplosione di Larry e Check e hanabi lo percula."

    hb "Se succede una volta è un'anomalia. {w}Due volte? Una coincidenza"

    show hnb fury
    hb "Siamo già alla terza volta di fila che il tuo assistente va fuori di testa con te beatamente allo scuro di tutto."

    ck "Mhhhhhhhhh..."

    show hnb smug devil cigar

    ck "Quella scena merita un bel replay."

    hide check
    hide hnb
    scene torakku onlayer underlayer
    show larry worried close transmitter onlayer underlayer at right
    show check plain angry shout onlayer underlayer at left
    show check fp onlayer underlayer at flip

    with dissolve

    hb "Hanananana! Guarda che faccia quando hai realizzato cosa stava succedendo."

    show check:
        easeout 0.7 xalign 0.6
        easein 0.7 xalign 0.0
        repeat

    hb "Avanti indietro avanti indietro avanti... {w}potrei rivederlo per giorni senza stancarmi!{p}HANANANANANANANANANNANANANANA!"

    hide check onlayer underlayer
    hide larry onlayer underlayer

    show check sor fp think worried at left
    show check at flip
    show hnb grin smug at right

    with dissolve

    hb "C'è da dire che pure quel Larry è un capolavoro di stupidità."

    hb "Che c'è? Ti sei circondato di gente ancora più incapace di te per sentirti meno sdatto? {w}Se questo è il livello medio del BKG, non serviva neanche un complotto per tirarlo giù."

    show check angry
    ck "Dì quello che vuoi, ormai so come funzionano le tue provocazioni! {w}Stai solo cercando di distrarmi così che io non possa trovare una contromossa."

    hb "Check... non lo hai capito? Il tempo che avevi è scaduto.{w} La partita è chiusa!"

    show hnb fury devil fist


    hb "Fine!{w} GAME OVER! "

    hide check
    hide hnb
    show torakku_grayscale
    show you_died

    extend "YOU DIED!!!"

    hb "E con questa tua sconfitta, la tua esistenza come coscienza superiore verrà terminata definitivamente!"

    hide torakku_grayscale
    hide you_died

    "Check tries to talk back but is somehow restrained"

    "the church rises up with a description and a very fitting sound effect"

    "parla degli errori"

    window hide
    pause 1

    hide check with Dissolve(1)
    camera at Shake((0, 0, 0, 0), 10.0, dist=10)
    show church_wall:
        ypos 1.5
        linear 5 ypos 0

    pause 5
    hide sky_frag
    hide church_wall

    show sky_frag with Dissolve(1)
    camera at Shake((0, 0, 0, 0), 10.0, dist=10)
    show church_wall at flip:
        ypos 1.5
        linear 5 ypos 0

    pause 6
    scene darkso_church with Dissolve(1)
    "stop"


    camera:
        xalign 0.5
        yalign 0.4
        ease 2 zoom 2

    pause 2

    show check sor p angry nope onlayer overlayer with squares


    ck "Non ancora… non è ancora finita..."

    hb "Ecco quali sono stati i tuoi più grandi errori durante questo gioco!"

    camera:
        zoom 1
        yalign 0.5
        xalign 0.5


    show sky_frag onlayer underlayer
    scene sisters:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    show stop_time behind check

    with purple_flash
    "Appaiono a a sfondo quando vengono criticati"


    hide sonozakitchen
    show rika_moon:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash
    ck "Rika è in combutta con questa misteriosa organizazione! Trae vantaggio dalle informazioni ottenute dalle riunioni dei Sonozaki a cui ha assistito per tramare i suoi loschi piani."

    show rika_moon:
        linear 0.5 zoom 0.3 xalign 0.1

    pause 1

    show rena_shion:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash

    ck "Rena è fanatica della maledizione di Oyashiro-Sama, e convince Shion a crederci! A causare il disastro ogni volta è Shion, suggestionata dalle parole di Rena! Sempre Rena ha suggestionato Keichi nel terzo frammento e lo ha fatto impazzire!"

    show rena_shion:
        linear 0.5 zoom 0.3 xalign 0.9

    pause 1

    show rika_shion:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    hb "NUMERO 1! Non sei riuscito ad individuare lo scambio tra Mion e Shion!"
    "(le gambe di Check vengono bloccate e legate da fili rossi, poi quello che appare a schermo ne discutiamo insieme)"
    "cg sorelle crack"

    hb "Shion Sonozaki si è Sostituita a Mion la notte dopo il Watanagashi! Era lei la colpevole per la serie di sparizioni ad Hinamizawa in questo frammento!"

    ck "nnnghhhhhh"

    "(Check viene incantenato da delle catene rosse)"

    hb "NUMERO 2! Non sei riuscito ad individuare il come mai!"

    "Fili rossi bloccano il resto del corpo"
    "cg shion pazza crack"

    hb "Ormai è ovvio, Shion ha agito di conseguenza alla follia che la ha assalità! Una follia che non puoi negare si causata dalla maledizione di Oyashiro-sama!"

    hb "Tutte le tue teorie su indottrinamenti vari erano sbagliate!"


    "(Intorno a Check emergono dal pavimento le pareti di una chiesa, cambia il BG)"
    "The screen rumbles heavily as walls are erected on both sides (2 cuts). Lastly we cut to check on the new background"

    hb "NUMERO 3! Non sei riuscito ad individuare il fatto che la famiglia Sonozaki non è responsabile per la serie di Omicidi ad Hinamizawa!"
    "Gli sprite con un effetto strano compaiono dietro. Poi si rompono"



    hb "Tutte le tue teorie su complotti di Rika, Rena, Satoko, misteriose organizazioni varie, si sono rivelate completamente, completamente prive di fondamento!"



    jump gk330
    return

