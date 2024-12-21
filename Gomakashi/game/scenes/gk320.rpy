label break_image:
    show frag_overlay onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    play sound "audio/sfx/glass crack.mp3"

    show check:
        linear 0.2 xoffset -100
        linear 1.2 xoffset 0

    pause 1.5
    play sound "audio/sfx/teleport.wav"

    return

label gk320:
    call hide_menu
    "------------scene 320 Metarivali part 1-------------"

    scene black onlayer underlayer
    scene witch_flowers
    with purple_flash
    play music "audio/umi/scorpion entrails.mp3"
#     play music "audio/umi/black liliana.mp3"
    play sound "audio/sfx/teleport.wav"
    show check sor fp think worried at left
    show check at flip
    show hnb yepper close at right
    with squares

    hb "Se succede una volta è un'anomalia. {w}Due volte? Una coincidenza"

    show hnb fury
    hb "Siamo già alla terza volta di fila che il tuo assistente va fuori di testa con te beatamente all'oscuro di tutto."

    ck "Mhhhhhhhhh..."

    show hnb smug devil cigar

    hb "Quella scena merita un bel replay."


    scene torakku onlayer underlayer
    show larry worried close transmitter onlayer underlayer at right
    hide check
    hide hnb
    show check plain angry shout onlayer underlayer at left
    show check fp onlayer underlayer at flip

    with purple_flash

    hb "Hanananana! Guarda la tua faccia quando hai realizzato cosa stava succedendo."

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


    hb "Fine della festa!{w} GAME OVER!"

    window hide
    hide check
    hide hnb
    show torakku_grayscale
    with purple_flash

    show you_died with Dissolve(3)



    hb "SEI MORTO!!!!!"
    hb "E stavolta non puoi premere continua! Questa è la fine della tua esistenza come coscienza superiore!"

    scene witch_flowers
    hide witch_flowers
    scene sky_frag onlayer underlayer

    show check sor fp angry shoutest at left
    show check at flip
    show hnb evilgrin fury at right

    with purple_flash

    ck "Non ancora... non è ancora finita..."
    ck "Non posso arrendermi ora... non posso perdere ora"

    show hnb fist devil
    hb "Se non riesci ancora ad accettare la realtà ti aiuterò io..."

    hb "Ripercorrendo tutti i tuoi più grandi errori nel corso di questo gioco!"

    play sound "audio/sfx/truth.mp3"
    hb "{color=#f00}ERRORE 1!{/color}"
    play sound "audio/sfx/teleport.wav"
    show sisters onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash
    hb "Non sei riuscito ad individuare lo scambio tra Mion e Shion prima che ti fosse rivelato!"

    hb "Shion Sonozaki si è Sostituita a Mion la notte dopo il Watanagashi! Era lei la colpevole per la serie di sparizioni ad Hinamizawa in questo frammento!"

    hb "Avresti dovuto accorgertene alla fine del secondo frammento, quando è stato confermato che Mion era già morta. {w}A quel punto c'era solo una possibile spiegazione."

    hb "Eppure era così ovvio! I gemelli che si scambiano sono uno dei clichè più vecchi!"


    call break_image

    hide sisters
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)

    show check worried
    ck "Nnnghhhhhh"

    show check t1 with dissolve

    ck "CHE DIAMINE è questo?! Non si toglie!"

    hb "È la prova del tuo errore! E non sarà l'ultima!"

    play sound "audio/sfx/truth.mp3"
    hb "{color=#f00}ERRORE 2!{/color}"
    play sound "audio/sfx/teleport.wav"
    show rena_shion onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    with purple_flash

    hb "Non sei riuscito ad individuare l'innocenza della famiglia Sonozaki!"

    show hnb -fist yepper
    hb "Ricordo bene come all'inizio eri sicuro di trovare la soluzione seguendo la pista di Mion."
    hb "Ti sei lasciato influenzare dalle teorie del complotto di Shion, e hai continuato a credere che fossero le tre famiglie a tirare le fila della maledizione. {w}Anche quando perfino sotto tortura, Mion e il sindaco si sono dichiarati innocenti."

    hb "E tutte quelle storie sull'indottrinamento del villaggio? {w}Mion, Rika, Rena, Satoshi... Non puoi più dire che sono stati educat per credere alla maledizione!"

    show hnb close
    hb "Dopotutto la confessione che hai visto era soltanto Shion che cercava disperatamente di giustificare le sue azioni. Ma lei a Hinamizawa non metteva piede da anni!"

    show hnb fury fist
    hb "Era la fantasia di una pazza assassina, non la verità!"

    show check think worried
    call break_image
    hide rena_shion
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    show check angry t2 with dissolve


    hb "Il che ci porta a...."

    play sound "audio/sfx/truth.mp3"
    hb "{color=#f00}ERRORE 3!{/color}"
    play sound "audio/sfx/teleport.wav"
    show mion_jumpscare onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    with purple_flash

    hb "Hai di nuovo fallito nell'individuare la causa della maledizione!"

    hb "Ormai è ovvio, Shion ha agito di conseguenza alla pazzia che la ha assalità! {w}Nessun piano premeditato, solo una follia distruttiva."

    hb "Cercando le prove di una serie di omicidi organizzati hai trovato solo l'ennesima vittima e carnefice. {w}Un caso da manuale dalla maledizione di Oyashiro-sama!"

    show check think worried
    call break_image
    hide mion_jumpscare
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    show check angry t3 with dissolve

    hb "Niente di quello che hai previsto si é verificato, e brancoli nel buio tanto quanto all'inizio!"

    "the church rises up with a description and a very fitting sound effect"
    "music change to moon"

    #---------------------------------
    #Church

    window hide
    pause 1

    hide check
    hide hnb
    hide sky_frag onlayer underlayer
    scene sky_frag
    with Dissolve(1)


    camera at Shake((0, 0, 0, 0), 10.0, dist=10)
    show church_wall:
        ypos 1.5
        linear 5 ypos 0

    pause 7
    hide church_wall

    camera at Shake((0, 0, 0, 0), 12.0, dist=10)
    show church_wall at flip:
        ypos 1.5
        linear 5 ypos 0

    pause 7
    scene darkso_church with Dissolve(1)

    pause 4
    camera:
        xalign 0.5
        yalign 0.4
        ease 2 zoom 2.3

    pause 2

    show check t1 t2 t3 sor p angry nope onlayer overlayer with squares:
        xalign 0.55


    hb "Tutte le tue teorie su complotti di Rika, Rena, Satoko, misteriose organizazioni varie, si sono rivelate completamente, completamente prive di fondamento!"


    play sound "audio/sfx/truth.mp3"
    hb "{color=#f00}ERRORE 4!{/color}"
    hb "Avere pensato per un solo momento che potessi farcela."
    jump gk330
    return

