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

label gk32:
    call hide_menu from _call_hide_menu_10

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
    ck "Non posso arrendermi ora... non posso perdere ora."

    show hnb fist devil
    hb "Se non riesci ancora ad accettare la realtà ti aiuterò io..."

    hb "Ripercorrendo tutti i tuoi più grandi errori nel corso di questo gioco!"

    play sound "audio/sfx/doon.mp3"
    hb "ERRORE 1!"
    play sound "audio/sfx/teleport.wav"
    show sisters onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    with purple_flash
    hb "Non sei riuscito ad individuare lo scambio tra Mion e Shion prima che ti fosse rivelato!"

    hb "Shion Sonozaki si è Sostituita a Mion la notte dopo il Watanagashi! Era lei la colpevole per la serie di sparizioni ad Hinamizawa in questo frammento!"

    hb "Avresti dovuto accorgertene alla fine del secondo frammento, quando è stato confermato che Mion era già morta. {w}A quel punto c'era solo una possibile spiegazione."

    hb "Eppure era così ovvio! I gemelli che si scambiano è uno dei clichè più vecchi e rivisti!"

    call break_image from _call_break_image

    hide sisters
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)

    show check worried
    ck "Nnnghhhhhh"

    show check shout t1 with dissolve

    ck "CHE DIAMINE è questo?! Non si toglie!"

    hb "È la prova del tuo errore! E non sarà l'ultima!"

    play sound "audio/sfx/doon.mp3"
    hb "ERRORE 2!"
    play sound "audio/sfx/teleport.wav"
    show mion_doll onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    with purple_flash

    hb "Non sei riuscito ad individuare l'innocenza della famiglia Sonozaki!"

    show hnb -fist yepper
    hb "Ricordo bene come all'inizio eri sicuro di trovare la soluzione seguendo la pista di Mion."
    hb "Ti sei lasciato influenzare dalle teorie del complotto di Shion, e hai continuato a credere che fossero le tre famiglie a tirare le fila della maledizione. {w}Anche quando perfino sotto tortura, Mion e il sindaco si sono dichiarati innocenti."

    hb "Sospettando la persona più innocente di tutti, Mion Sonozaki."
    show hnb close
    hb "Anche la confessione con cui ti sei difeso all'inizio era soltanto lei che cercava disperatamente di giustificare le sue azioni."

    show hnb fury fist
    hb "Era la fantasia di una pazza assassina, non la verità!"



    show check think worried
    call break_image from _call_break_image_1
    hide mion_doll
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    ck "Gaahhr!"
    show check angry t2 with dissolve

    ck "Toglimi subito queste robe di dosso altrimenti..."
    hb "Altrimenti cosa?"
    hb "E non abbiamo finito. {w}Ricordi tutte quelle teorie sull'indottrinamento del villaggio che erano il tuo cavallo di battaglia?"
    hb "Mion, Rika, Rena, Satoshi...{w} con i leader del villaggio scaggionati non puoi più dire che sono stati educati dall'infanzia credere alla maledizione!"
    hb "Il che ci porta a...."

    play sound "audio/sfx/doon.mp3"
    hb "ERRORE 3!"
    play sound "audio/sfx/teleport.wav"
    show mion_jumpscare onlayer underlayer:
        zoom 0.5
        xalign 0.5
        yalign 0.3
    with purple_flash

    show hnb evilgrin -fist
    hb "Hai di nuovo fallito nello spiegare la maledizione di Oyashiro sama!"

    hb "Ormai è ovvio, Shion ha agito di conseguenza alla pazzia che la ha assalità! {w}Nessun piano premeditato, solo una follia distruttiva."

    hb "Cercando le prove di una serie di omicidi organizzati hai trovato solo l'ennesima vittima e carnefice. {w}Un caso da manuale dalla maledizione di Oyashiro-sama!"

    hb "Inoltre, sospettando la persona più innocente di tutti, Mion Sonozaki, hai trascurato la raccolta di indizi sugli altri quesiti irrisolti. Come il perché Rika è in grado di prevedere tutti gli omicidi!"


    show check think worried
    call break_image from _call_break_image_2
    hide mion_jumpscare
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    show check angry t3 with dissolve

    hb "Niente di quello che hai previsto si é verificato, e brancoli nel buio tanto quanto all'inizio!"

    hb "Questo può essere descritto in un solo modo!!!!!!{p}FALLIMENTO TOTALE!!!!!"

    hb "E una una performance così terribile richiede una punizione adatta!!!!!"

    show hnb fist devil
    play sound "audio/sfx/truth.mp3"
    stop music
    play music ["<silence 2>","audio/higu/chimamireta chinkon uta.mp3"] fadein 4
    hb "LA PENA CAPITALE!"
    ck "COME SCUSA?!?!"

    show hnb yepper
    hb "Ma prima dobbiamo allestire la scena...{w} Ti presento il tuo ultimo palcoscenico, nonché la tua tomba!"


    #---------------------------------
    #Church

    window hide
    pause 1

    hide check
    hide hnb
    hide sky_frag onlayer underlayer
    scene sky_frag
    with Dissolve(1)
    play sound "audio/sfx/earth rumbling.mp3" volume 2

    camera at Shake((0, 0, 0, 0), 10.0, dist=10)
    show church_wall:
        ypos 1.5
        linear 5 ypos 0

    $renpy.pause(7, hard=True)
    hide church_wall with pushleft

    camera at Shake((0, 0, 0, 0), 12.0, dist=10)
    show church_wall at flip:
        ypos 1.5
        linear 5 ypos 0

    $renpy.pause(7, hard=True)
    scene darkso_church with pushright

    stop sound fadeout 4
    $renpy.pause(4, hard=True)

    camera:
        xalign 0.5
        yalign 0.4
        ease 2 zoom 2.3

    $renpy.pause(2, hard=True)

    show check t1 t2 t3 sor p angry shoutest onlayer overlayer with squares:
        xalign 0.55

    ck "UNA CHIESA?!"

    window hide
    camera:
        xalign 0.5
        yalign 0.5
        zoom 1
    hide check onlayer overlayer
    show organ

    with Dissolve(2)
    pause 2

    show hnb evilgrin fury with squares
    hb "Grazie a quei marchi, dimostrazioni dei tuoi fallimenti, il prossimo sarà un attacco da cui non potrai difenderti, nasconderti o fuggire!"
    hb "Sorelle della battaglia! Suonate il vostro organo e cantate la sinfonia che oblitererà questo povero stolto una volta per tutte!"

    play sound "audio/sfx/moving_tank.mp3" volume 0.7
    camera at Shake((0, 0, 0, 0), 20.0, dist=5)
    show organtank with dissolve
    $renpy.pause(8, hard=True)
    stop sound

    scene darkso_church
    show check t1 t2 t3 sor p angry shoutest onlayer overlayer
    camera:
        xalign 0.5
        yalign 0.4
        zoom 2.3
    with dissolve
    ck "COSA CAVOLO DANNAZZIONE CRIBBIO DIAMINE È QUELLO?!?!?!?!"


    camera:
        xalign 0.5
        yalign 0.5
        zoom 1
    hide check onlayer overlayer
    show organ
    show hnb devil fury

    hb "E adesso sarà rivelato il tuo ultimo e più grande {nw}"
    play sound "audio/sfx/doon.mp3"
    extend "ERRORE!!!"
    camera:
        xalign 0.5
        yalign 0.15
        linear 0.2 zoom 2.3
    hb "Avere pensato per un solo momento di potercela fare. {p}HANANANANANANANANNAANANANNANAANANANANANANANANANANANANANNANANA"


    camera:
        parallel:
            easein 0.6 yalign 0.5
        parallel:
            easein 0.4 zoom 1
    pause 0.2
    show hnb fist with Dissolve(0.3)
    hb "Sorelle.... FUOCO!"


    camera at Shake((0, 0, 0, 0), 20.0, dist=3)
    show organtank with dissolve

    $renpy.pause(3, hard=True)
    show missile_swarm with pushdown

    n "E fu così che con un frastuono assordante e una luce abbagliante, uno sciame di missili si levò verso il cielo."

    hide missile_swarm
    hide organtank
    show hnb devil fury
    with pushup

    hb "Hai un minuto di tempo per dire le tue ultime preghiere prima che i missili radano al suolo questo posto. {w}Fallo contare."

    stop music fadeout 3

    scene darkso_church
    show check t1 t2 t3 sor p angry shoutest onlayer overlayer
    camera:
        xalign 0.5
        yalign 0.4
        zoom 3

    camera overlayer:
        xalign 0.45
        yalign 0.1
        zoom 2
    with Dissolve(2)

    show check t4 worried with Dissolve(2)
    play music "audio/higu/testament.mp3" fadein 3

    ck "........"
    show check think
    ck "Se questa è la mia fine, voglio lasciare un messaggio alla strega che mi ha tanto aiutato."
    ck """Mi dispiace Bern... la sola cosa di cui mi pento in tutta questa storia è di averti delusa.

Mi hai scelto come tuo campione, come tua carta vincente, mi hai mostrato il mare dei frammenti e fatto scoprire il potere che avevo ottenuto da esso.

E io non ho saputo darti altro che sconfitta e umiliazione.

Se per qualche miracolo mi dovessi salvare farò qualsiasi cosa per sdebitarmi.

Grazie di tutto Bern... e scusami per la mia debolezza.
"""

    show check angry smile
    ck "E tu Hanabi... Credevo che il nostro prossimo duello sarebbe stato alle porte del Valhalla. Ma sembra che il destino avesse altri piani in serbo per noi."

    ck "So che mi odi per le scelte che ho fatto, ma sappi che non mi è dispiaciuto confrontarmi ancora una volta con te."

    ck "Sono pronto!!!!"

    camera:
        xalign 0.5
        yalign 0.5
        zoom 1

    hide check onlayer overlayer
    show missile_swarm

    with dissolve
    n "Raggiunto il picco della parabola, la pioggia di missili si dirisse in picchiata verso il suolo."

    n "Cosa passò per la mente di check mentre guardava la sua fine avvicinarsi? {w}Questo purtroppo non lo sapremo mai, ma si narra che in fondo fosse soddisfatto."



    show organ
    show hnb nope fury
    camera:
        xalign 0.2
        yalign 0.15
        zoom 2.3
        linear 11 xalign 0.8


    with Dissolve(3)
    $renpy.pause(5, hard=True)

    scene darkso_church
    show check t1 t2 t3 sor p angry nope onlayer overlayer
    camera:
        xalign 0.6
        yalign 0.4
        zoom 3
        linear 10 xalign 0.4

    camera overlayer:
        xalign 0.7
        yalign 0.1
        zoom 3
        linear 13 xalign 0.3

    with Dissolve(3)



    $renpy.pause(4, hard=True)


    play sound "audio/sfx/explosion.mp3" volume 0.6
    stop music fadeout 8
    show white
    $ renpy.transition(Dissolve(3), layer="master")

    show white onlayer overlayer
    $ renpy.transition(Dissolve(6), layer="overlayer")


    $renpy.pause(10, hard=True)
    n "Così come della chiesa non rimase che un cumulo di macerie e cenere. Anche le ambizioni del detective che si oppose al fato furono ridotte a niente più che una colonna di fumo nell'aria."

    hide white
    hide check
    camera:
        xalign 0.5
        yalign 0.5
        zoom 1
    stop music fadeout 10
    scene bern_fancy with Fade(5,1,5)
    play music "audio/umi/about face.mp3"
    play sound "audio/sfx/teleport.wav"
    show bern yoko at left
    show lamb at right
    with squares


#     n "Così come della chiesa non rimase che un cumulo di macerie e cenere. Anche le ambizioni del detective che si oppose al fato furono ridotte a niente più che una colonna di fumo nell'aria."

    ld "Veramente un finale strappalacrime. {w}Non ti sembra Bern? {w}Peccato che avevi già perso e non hai potuto vederlo."

    bk "Lasciami indovinare, nel tuo caso sono lacrime dalle troppe risate vero?"

    show lamb cat
    ld "Ehe! Inizi a conoscermi."

    ld "Certo che potresti essere un po'più sensibile. {w}Ti ha pure dedicato le sue ultime parole prima di schiattare, se solo le mie pedine fossero così leali e obbedienti."
    show bern chira
    bk "Che brutta personalità, eppure conosci meglio di me le implicazioni di questo esito."

    show bern yoko
    bk "Oppure vuoi soltanto sprecare il mio tempo?"

    ld "Bene, non vedo l'ora di vedere quale sia la tua prossima mossa. {w}Spero che sia qualcosa di più interessante di quei due."

    bk "Non ho nessuna obbligazione di mantenere le tue aspettative..."



    stop music fadeout 10
    scene black with longFade


    camera underlayer:
        xalign 0.5
        yalign 0.5
        zoom 1

    camera overlayer:
        xalign 0.5
        yalign 0.5
        zoom 1

    camera:
        xalign 0.5
        yalign 0.5
        zoom 1


    jump gkCredits
    return

