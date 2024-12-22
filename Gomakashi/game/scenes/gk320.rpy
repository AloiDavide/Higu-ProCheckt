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

    hb "Sospettando la persona più innocente di tutti, Mion Sonozaki"
    show hnb close
    hb "Anche la confessione con cui ti sei difeso all'inizio era soltanto lei che cercava disperatamente di giustificare le sue azioni."

    show hnb fury fist
    hb "Era la fantasia di una pazza assassina, non la verità!"



    show check think worried
    call break_image
    hide rena_shion
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    ck "Gaahhr!"
    show check angry t2 with dissolve

    hb "Ricordi tutte quelle teorie sull'indottrinamento del villaggio che erano il tuo cavallo di battaglia?"
    hb "Mion, Rika, Rena, Satoshi...{w} con i leader del villaggio scaggionati non puoi più dire che sono stati educati dall'infanzia credere alla maledizione!"
    hb "Il che ci porta a...."

    play sound "audio/sfx/truth.mp3"
    hb "{color=#f00}ERRORE 3!{/color}"
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
    call break_image
    hide mion_jumpscare
    hide frag_overlay
    with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)
    show check angry t3 with dissolve

    hb "Niente di quello che hai previsto si é verificato, e brancoli nel buio tanto quanto all'inizio!"

    hb "Questo può essere descritto in un solo modo!!!!!!{w} FALLIMENTO TOTALE!!!!! {w}E c'è una sola punizione adatta per una performance così terribile!!!!!"

#     play music "audio/higu/moon.mp3"
    play music "audio/higu/chimamireta chinkon uta.mp3"

    #---------------------------------
    #Church

    window hide
    pause 1

    hide check
    hide hnb
    hide sky_frag onlayer underlayer
    scene sky_frag
    with Dissolve(1)
    play sound "audio/sfx/earth rumbling.mp3" volume 1.5

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

    stop sound fadeout 4
    pause 4

    camera:
        xalign 0.5
        yalign 0.4
        ease 2 zoom 2.3

    pause 2

    show check t1 t2 t3 sor p angry shoutest onlayer overlayer with squares:
        xalign 0.55

    ck "UNA CHIESA?!"

    camera:
        xalign 0.5
        yalign 0.5
        zoom 1
    hide check onlayer overlayer
    show organ
    show hnb evilgrin fury
    with dissolve
    hb "Grazie a quei marchi, dimostrazioni dei tuoi fallimenti, il prossimo sarà un attacco da cui non potrai difenderti, nasconderti o fuggire!"
    hb "Sorelle della battaglia! Suonate il vostro organo e cantate la sinfonia che oblitererà questo povero stolto una volta per tutte!"

    play sound "audio/sfx/moving_tank.mp3" volume 0.7
    camera at Shake((0, 0, 0, 0), 20.0, dist=5)
    show organtank with dissolve
    pause 8
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


    play sound "audio/sfx/truth.mp3"
    hb "E adesso sarà rivelato il tuo ultimo e più grande {color=#f00}ERRORE!!!{/color}"
    camera:
        xalign 0.55
        yalign 0.15
        linear 0.2 zoom 2.3
    hb "Avere pensato per un solo momento di potercela fare. {p}HANANANANANANANANNAANANANNANAANANANANANANANANANANANANANNANANA"

    hb "Hai un minuto di tempo per dire le tue ultime preghiere. {w}Fallo contare."
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

    ck """Mi dispiace Bern... la sola cosa di cui mi pento in tutta questa storia è di averti delusa.

Mi ahi scelto come tuo campione, come tua carta vincente, mi hai mostrato il mare dei frammenti e fatto scoprire il potere che avevo ottenuto da esso.

E io non oh saputo darti altro che sconfitta e umiliazione.

Se per qualche miracolo mi dovessi salvare farò qualsiasi cosa per sdebitarmi.

Grazie di tutto Bern...e scusami per la mia debolezza
"""

    show check angry smile
    ck "E tu Hanabi... Credevo che il nostro prossimo duello sarebbe stato alle porte del Valhalla. Ma sembra che il destino avesse altri piani in serbo per noi."

    ck "So che mi odi per le scelte che ho fatto, ma sappi che non mi è dispiaciuto confrontarmi ancora una volta con te."

    ck "Sono pronto....... FAI DEL TUO PEGGIO!"

    camera:
        xalign 0.5
        yalign 0.5
        zoom 1
    hide check onlayer overlayer
    show organ
    show hnb nope fury
    with Dissolve(2)
    hb "Sorelle.... FUOCO!"

    camera at Shake((0, 0, 0, 0), 20.0, dist=3)
    show organtank with dissolve

    pause 2
    show missile_swarm with pushdown

    n "E fu così che con un frastuono assordante e una luce abbagliante, una pioggia di missili si levò verso il cielo e si abbattè sull'ormai inerme Check."

    n "Così come della chiesa non rimase che un cumulo di macerie e cenere. Anche le ambizioni di quell'uomo furono ridotte a niente più che una colonna di fumo nell'aria."

    stop music fadeout 10
    scene bern_fancy with Fade(5,5,5)
    play music "audio/umi/about face.mp3"
    play sound "audio/sfx/teleport.wav"
    show bern yoko at left
    show lamb at right
    with squares

    ld "Veramente un finale strappalacrime. {w}Non ti sembra Bern? {w}Peccato che avevi già perso e non hai potuto vederlo."

    bk "Lasciami indovinare, nel tuo caso sono lacrime dalle troppe risate vero?"

    show lamb cat
    ld "Ehe! Inizi a conoscermi."

    ld "Certo che potresti essere un po'più sensibile. {w}Ti ha pure dedicato le sue ultime parole prima di schiattare, se solo le mie pedine fossero così leali e obbedienti."
    show bern chira
    bk "Che brutta personalità, eppure conosci meglio di me le implicazioni di questo esito."

    show bern yoko
    bk "Oppure vuoi soltanto sprecare il mio tempo?"

    stop music fadeout 6
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
    jump credits_scene
    return

