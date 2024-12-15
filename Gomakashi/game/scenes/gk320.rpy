label gk320:
    call hide_menu
    "------------scene 320 Metarivali part 1-------------"
    scene sky_frag
    show check sor p angry nope
    play music "audio/umi/red dread.mp3"
    "Esce dalla esplosione di Larry e Check e hanabi lo percula."

    hb "Se non sbaglio questa è la terza volta di fila che il tuo assistente va fuori di testa con te completamente allo scuro."

    hb "Che c'è? Ti sei circondato di gente ancora più incapace di te per sentirti meno sdatto? {w}Se questo è il livello medio del BKG, non serviva neanche un complotto per tirarlo giù."

    ck "Silenzio! Anche se di me puoi dire quello che vuoi non hai il diritto di criticare i miei sottoposti."

    hb "Check... questa è una totale sconfitta!"

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

