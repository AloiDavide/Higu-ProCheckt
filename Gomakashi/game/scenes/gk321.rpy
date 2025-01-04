label gk321:
    call hide_menu from _call_hide_menu_11
    play music "audio/sfx/wind.mp3" fadein 5
    scene gael_arena
    show smoke onlayer overlayer
    with longFade
    "------------scene 321 Metarivali part 2-------------"


    show hnb nopper at right

    with dissolve
    hb "Diamine!"

    hide smoke onlayer overlayer
    $ renpy.transition(Dissolve(20), layer="overlayer")

    hide hnb
    show hnb_pacing
#     show hnb cigar:
#         ease 2 left
#         pause 0.5
#         flip with dissolve
#         pause 0.3
#         ease 2 right
#         pause 0.5
#         unflip
#         pause 0.3
#         repeat 5
    hb "Questo non era previsto... ma almeno adesso è sistemato sia all'interno che all'esterno."

    hb "Guarda che faccia tosta, pure da morto continua a causarmi problemi... {w}mi ha pure costretto a uscire allo scoperto."
    hb "Che urto! Che irritazione!"


    hb "...Ed ora come cavolo esco da qui?"


    n "Per qualche motivo, Hanabi aveva ancora un brutto presentimento."


    hb "Mhhhh..."
    hide hnb_pacing
    show hnb ohno nopper at left
    play music "audio/umi/dread of the grave.mp3"

    hb "NO! IMPOSSIBILE!"
    play sound ["audio/sfx/furu.ogg","audio/sfx/down.ogg"]
    camera at sshake

    show check fire shout p:
        offscreenright
        ease 0.2 xalign 0.3
    pause 0.2
    show hnb:
        ease 0.2 offscreenleft
    show check:
        ease 0.6 center
    n "Nonostante i suoi acuti sensi e riflessi, non fece in tempo a scansarsi, e la forza del montante lo scaraventò a terra."




    ck "MA CHI DIAVOLO TI CREDI DI ESSERE PER PENSARE DI POTERMI SCONFIGGERE COSÌ FACILMENTE!!!"
    show check shoutest
    play sound "audio/sfx/short doon.mp3" volume 1.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.3
    ck "CREDEVI CHE QUESTO FOSSE TUTTO QUELLO CHE POSSO FARE? CREDEVI VERAMENTE CHE FOSSE COSÌ FACILE SBARAZZARTI DI ME?????"

    ck "NEANCHE PER SOGNO! LA NOSTRA BATTAGLIA È SOLO INIZIATA!!!"
    play sound "audio/sfx/short doon.mp3" volume 1.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.6
    ck "AVRAI VINTO LA BATTAGLIA MA NON HAI VINTO LA GUERRA! TUTTO QUELLO CHE è SUCCESSO FINORA NON È STATO ALTRO CHE UNA PREPARAZIONE PER LA TUA TOTALe SCONFITTA NELLA PROSSIMA PARTITA!!!"
    play sound "audio/sfx/short doon.mp3" volume 1.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.9
    ck "NON SONO MAI STATO ARRABBIATO QUANTO IN QUESTO MOMENTO, LA PAGHERAI PER TUTTI I TUOI CRIMINI E LE TUE CRUDELTÀ!!!"
    ck "LA PROSSIMA VOLTA TI TRASFORMERÒ IN UN MUCCHIETTO DI POLVERE!!! SEI PRONTO????"
    window hide
    camera:
        easein 1 zoom 1
    pause 1
    camera at Shake((0, 0, 0, 0), 4.0, dist=15)

    play sound "audio/sfx/aura.mp3"

    show debris behind check, hnb:
        ypos 1080
        easeout 3 ypos 0
    pause 0.5
    ck "UUOOOOOOOOOOOHH!!!!!!!!!!!!!!"

    "(L' aura di Check esplode fino a spostare Hanabi, la scena dietro di loro si incrina.{color=f37530}(?){/color})"
    show check:
        ease 1 right

    show hnb napalm_right fury nopper at flip:
        ease 1 left
    pause 1
    hb "Ma come diavolo... io dovrei avere vinto! Come cavolo fai ad essere ancora qui!"

    ck "IO NON PERDO FINO A CHE NON SMETTO DI RIALZARMI, SONO STATO CHIARO? NON ESISTE LA SCONFITTA NEL MIO VOCABOLARIO!!!"
    show check shout

    ck "Non avrò risolto tutto questa volta, ma ora ho accesso a delle informazioni cruciali con cui interpretate gli altri frammenti!"
    ck "Lo scambio delle gemelle! l'innocenza dei Sonozaki! l'attacco di Rika!"

    show check objection at pointing with purple_quick:
        xoffset 300


    ck "E soprattutto tu Hanabi! Tu sei vivo ad Hinamizawa e sei parte della cospirazione ai danni del BKG!"
    hide check
    show check fire shout p at right
#     show torakku_grayscale behind check, hnb

    with purple_flash

    show you_died behind check, hnb:
        yoffset -300
    $ renpy.transition(Dissolve(2))

    hb "Sta zitto! Non vedi che sei morto di nuovo?"


    ck "Ogni morte è una lezione Hanabi."
    play sound "audio/sfx/glass crack.mp3"
    hide you_died with ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5)

    ck "Questa volta io e Larry ci siamo andati così vicini che sei stato costretto a rivelare la tua mano. {w}Una via di uscita esiste, e noi la troveremo, non importa quanti tentativi ci vorranno!"


    hb "Ggghhh... ma allora quale diavolo è la mia condizione di vittoria! Dannazione!"




    scene bern_fancy with fade
    play music "audio/umi/about face.mp3"
    play sound "audio/sfx/teleport.wav"
    show bern yoko at left
    show lamb at right
    with squares

    bk "Certamente non credevi anche tu che Check sarebbe semplicemente scomparso."

    ld "Ma figurati, quello è testardo quasi quanto te."

    ld "Hai legato la sua esistenza alla tua a tal punto che l'unico modo per distruggerlo ormai è la tua sconfitta. {color=f37530}(Forshadowing a check che si autodistrugge con bernkastel?){/color}"

    ld "Ecco perchè ho scelto di separarvi, geniale vero?"
    show lamb yep


    bk "E di tutto questo suppongo che non avrai detto una parola ad Hanabi."
    show lamb smirk evil
    ld "Alla fine non è altro che il mio burattino! {w}Anche se non può vincere, tutto quello che deve fare è restare imprigionato in un ciclo eterno di battaglie fino a che la mia partita non è finita! Fin dall' inizio era questo il suo scopo!"

    bk "In altre parole, un destino peggiore della morte."

    "(lambdadelta da un frammento)"


    show hnb evilgrin fury at right onlayer overlayer
    show check angry nope fp at left onlayer overlayer
    show check at flip

    show vs_screen
    show tsumi_prop:
        zoom 0.3
        xalign 0.5
        yalign 0.0

    show hnb:
        xoffset -450
        yoffset 180
    show check:
        xoffset 280
        yoffset 230
    camera overlayer:
        zoom 2
        xalign 0.5
        yalign 0.5
    play sound "audio/sfx/zbiin.ogg"

    window hide
    pause 1
    play music "audio/umi/dread of the grave.mp3"
    hb "Molto bene! Allora come stabilito stavolta sono io a decidere chi sarà la tua prospettiva!"
    hb "Perfetto. PROSSIMA PARTITA!"
    ck "MOLTO BENE! NON PERDERÒ PER NESSUNA RAGIONE AL MONDO! PROSSIMA PARTITA!"

    window hide
#     show black onlayer overlayer with Dissolve(1):
#         alpha 0.6


    pause 0.3

    camera:
        xalign 0.5
        yalign 0.0
        easeout_expo 1.5 zoom 3

    camera overlayer:
#         easeout_expo 1.5 yalign -0.4
        easeout_expo 1.5 zoom 6

    pause 1.5

    hide check
    hide hnb

    camera:
        zoom 1
    scene tsumi_frag

    play sound "audio/sfx/doon.mp3" volume 1.5

    stop music fadeout 35
    $renpy.transition(vpunch)
    $renpy.call_screen('welcome_tsumi')

    return