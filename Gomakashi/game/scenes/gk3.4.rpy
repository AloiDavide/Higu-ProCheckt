label gk34:
    call hide_menu from _call_hide_menu_11
    play music "audio/sfx/wind.mp3" fadein 5
    scene gael_arena
    show smoke onlayer overlayer
    with longFade
    show hnb nopper at right

    with dissolve
    hb "Dannazione!"

    hide smoke onlayer overlayer
    $ renpy.transition(Dissolve(30), layer="overlayer")

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

    n "Sebbene Hanabi avesse raggiunto il suo obiettivo ultimo, non riusciva a ritenersi soddisfatto."

    n "Tutti i suoi sensi, dal primo al sesto, gli urlavano che qualcosa non andava, e di non abbassare la guardia."


    hide hnb_pacing
    show hnb nopper at left

    hb "....Ho un brutto presentimento. {w}Devo trovare un modo di uscire da quì."

    hb "........"
    show hnb ohno
    play music "audio/umi/dread of the grave.mp3"

    hb "NO! IMPOSSIBILE!!!"
    play sound ["audio/sfx/furu.ogg","audio/sfx/down.ogg"]
    camera at sshake

    show check fire shout p:
        ypos 1.0
        xalign 1.2
        parallel:
            ease 0.2 ypos 0.0
        parallel:
            ease 0.2 xalign 0.3
    pause 0.2
    show hnb:
        ease 0.2 offscreenleft
    show check:
        ease 0.6 center

    pause 1


    ck "MA CHI DIAVOLO TI CREDI DI ESSERE PER PENSARE DI POTERMI SCONFIGGERE COSÌ FACILMENTE!!!"
    n "Nonostante Hanabi avesse percepito la presenza di Check tra le macerie, l'incredulo stupore rallentò i suoi riflessi sovraumani a tal punto da non permettergli di evitare l'attacco, e la forza di un montante supersonico lo scaraventò a terra."


    show check shoutest
    play sound "audio/sfx/short doon.mp3" volume 2.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.3
    ck "CREDEVI CHE QUESTO FOSSE TUTTO QUELLO CHE POSSO FARE? CREDEVI VERAMENTE CHE FOSSE COSÌ FACILE SBARAZZARTI DI ME?????"

    ck "NEANCHE PER SOGNO! LA NOSTRA BATTAGLIA È SOLO INIZIATA!!!"
    play sound "audio/sfx/short doon.mp3" volume 2.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.6
    ck "AVRAI VINTO LA BATTAGLIA MA NON HAI VINTO LA GUERRA! TUTTO QUELLO CHE è SUCCESSO FINORA NON È STATO ALTRO CHE UNA PREPARAZIONE PER LA TUA TOTALE SCONFITTA NELL PROSSIMO ROUND!!!"
    play sound "audio/sfx/short doon.mp3" volume 2.5
    camera:
        xalign 0.5
        yalign 0.0
        zoom 1.9
    ck "NON SONO MAI STATO ARRABBIATO QUANTO IN QUESTO MOMENTO, LA PAGHERAI PER TUTTI I TUOI CRIMINI E LE TUE CRUDELTÀ!!!"
    ck "LA PROSSIMA VOLTA TI TRASFORMERÒ IN UN MUCCHIETTO DI POLVERE!!! SEI PRONTO????"

    play sound "audio/sfx/earth rumbling.mp3" volume 1.5
    window hide
    camera:
        easein 1 zoom 1
    pause 1
    camera at Shake((0, 0, 0, 0), 4.0, dist=15)



    show debris behind check, hnb:
        ypos 1080
        easeout 3 ypos 0
    pause 0.5
    ck "UUOOOOOOOOOOOHH!!!!!!!!!!!!!!"
    stop sound fadeout 3

    show check:
        ease 1 right

    show hnb napalm_right ultrarage fury at flip:
        ease 1 left
    pause 1
    hb "Ma come diavolo... io dovrei avere vinto! Come cavolo fai ad essere ancora qui!"

    ck "IO NON PERDO FINO A CHE NON SMETTO DI RIALZARMI, SONO STATO CHIARO? NON ESISTE LA SCONFITTA NEL MIO VOCABOLARIO!!!"
    show check shout

    ck "Non avrò risolto tutto questa volta, ma ora ho accesso a delle informazioni cruciali con cui interpretate gli altri frammenti!"
    ck "Lo scambio delle gemelle! l'innocenza dei Sonozaki! l'attacco di Rika!"

    camera at sshake
    play sound "audio/sfx/short doon.mp3" volume 2.5

#
#     scene pros_stand
#     show check objection p fire shoutest:
#         xalign 0.8
#     show lawyer_table at flip
#
#
#
#     with purple_flash
#     pause 1
    play sound "audio/sfx/zbiin.ogg"
    play custom_audio "audio/sfx/aura.mp3" volume 2 loop
    show bubbling_aura_blue behind check
    show bubbling_aura_blue at right:
        xoffset 90
        yoffset 350
    ck "E SOPRATTUTTO TU HANABI! {w}Tu sei vivo ad Hinamizawa e sei parte della cospirazione ai danni del BKG!"

    play sound "audio/sfx/damage2.mp3" volume 2.5
    show hnb nopper at flip:
        linear 0.2 xoffset -150
        linear 1.2 xoffset 0

    pause 2

#     play sound "audio/sfx/short doon.mp3" volume 2.5
#     scene def_stand
#     show hnb napalm_right ultrarage fury at flip
#     show lawyer_table
#

#     pause 1.5


    hb "STA ZITTO! Non vedi che sei morto di nuovo?"
    show hnb grin
    show you_died:
        yoffset -0
    $ renpy.transition(Dissolve(1))

    pause 1

    hb "Cosa vuoi che cambi se questa volta sei sopravvissuto un po più a lungo? {w}Non hai potuto fare niente per cambiare il risultato."



#     show torakku_grayscale behind check, hnb


#



    show you_died behind check, bubbling_aura_blue
    with dissolve
    show hnb ultrarage
    show check:
        ease 1 center
    show bubbling_aura_blue:
        ease 1 xalign 0.4
    pause 1
    ck "Ogni morte è una lezione Hanabi."
    ck "Questa volta io e Larry ci siamo andati così vicini che sei stato costretto a rivelare la tua mano."

    ck "Una via di uscita esiste, e giuro che noi la troveremo! Non importa quanti tentativi ci vorranno!"
    show check shoutestOpen
    show hnb at flip:
        ease 0.3 offscreenleft
    show bubbling_aura_blue:
        parallel:
            easeout 0.2 xzoom 2.3
        parallel:
            easeout 0.2 xoffset 0

#     play sound "audio/sfx/glass crack.mp3"
    play sound ["audio/sfx/truth.mp3"]
#     play sound "audio/sfx/strike.mp3"
    with Dissolve(0.01)
    hide you_died
    $ renpy.transition(ImageDissolve(im.Scale("overlay/disintegrate.png", 1920, 1080), 1.5), layer="master")

    ck "HAAAAAAAAAAAAH!"

    window hide
    show check shoutest
    show bubbling_aura_blue:
        parallel:
            easeout 1 xzoom 1
        parallel:
            easeout 1 xoffset 90
    $renpy.pause(1, hard=True)
    show hnb nopper at flip:
        ease 1 left
    show check:
        ease 1 right
    show bubbling_aura_blue:
        ease 1 right

    show hnb fury
    hb "Ggghhh... tu davvero non sai quando mollare."

    hb "Ma allora quale diavolo è la mia condizione di vittoria! Dannazione!"
    show hnb ultrarage
    stop music fadeout 3
    n "............................."

    stop custom_audio fadeout 3
    scene bern_fancy with pushdown
    play music "audio/umi/the candles dance.mp3" fadein 1

    pause 1
    play sound "audio/sfx/teleport.wav"
    show bern yoko at left
    show lamb at right
    with squares

    bk "Certamente non credevi anche tu che Check sarebbe semplicemente scomparso."

    ld "Ma figurati, quello è testardo quasi quanto te."

    ld "Hai legato la sua esistenza alla tua a tal punto che l'unico modo per distruggerlo ormai è la tua sconfitta."

    ld "Ecco perchè ho scelto di separarvi, geniale vero?"


    bk "Tuttavia adesso Check conosce l'identità della prima delle tue cosiddette barriere: \"L'inganno dei Sonozaki\"."
    show lamb unhappy smirk

    ld "E allora? {w}Tu la conoscevi fin dall'inizio e comunque non hai potuto farci niente."
    ld "E poi le barriere sono tre per un motivo. È insieme che formano una certezza inespugnabile."

    ld "Check potrebbe provare per altri cento anni, ma non arriverà mai a una soluzione da solo."

    bk "Di tutto questo suppongo che non avrai detto una parola ad Hanabi."
    show lamb evil mad
    ld "Alla fine non è altro che il mio burattino!"

    ld "Che importa se non può vincere, tutto quello che deve fare è restare imprigionato in un ciclo eterno di battaglie fino a che la nostra sfida non sarà finita!"

    ld "A quel punto lo rilancerò nell'abbisso da cui è venuto. Problema risolto."

    bk "In altre parole, un destino peggiore della morte...."



    stop music fadeout 2
    pause 2

    scene gael_arena
    show bubbling_aura_blue at right:
        xoffset 90
        yoffset 350
    show hnb fury nope napalm_right at left
    show hnb at flip
    show check fire nope p at right


    with pushup

    n "..........................................................{p}.........................................................."
    play music "audio/umi/endless nine.mp3" fadein 2
    show hnb evilgrin fury
    hb "Hanana.{w} HANANANANANANANA!!!"

    hb "Benissimo! Accetto la sfida!"
    play custom_audio "audio/sfx/aura.mp3" volume 2 loop
    play sound "audio/sfx/zbiin.ogg"
    show bubbling_aura_red behind hnb:
        xoffset -180
        yoffset -150

    hb "Distruggerò le tue illusioni ancora ed ancora, fino a che non avrai più la forza di rialzarti."

    show check smile
    ck "Cosa stiamo aspettando? Sono pronto al prossimo round. {w}La scorsa partita ho scelto io il campo di battaglia, questa volta tocca a te."

    hb "Ti ho visto parecchio curioso su Rena. {w}Beh perchè no, sarà lei la prossima che seguiremo!"

    hb "E voi streghe, ci date un frammento o dobbiamo venire a prenderlo?"


    stop custom_audio fadeout 2
    scene bern_fancy with pushdown

    show bern yoko at left
    show lamb unhappy pout at right


    ld "Guarda che faccia tosta."
    show lamb smirk
    ld "Se si parla di Rena... Sai già che tipo di frammento sceglierò vero?"


    play sound "audio/sfx/teleport.wav"
    show tsumi_prop:
        zoom 0.3
        xalign 0.5
        yalign 0.5
    with squares

    pause 1

    bk "Fai come preferisci, non mi interessa."

    ld "Oh vedrai sarà esilarante, una tragedia così ironica da strappare una risata perfino a te."

    "{color=#f37530}Lambdadelta sa che alla fine Keiichi farà rinsanire Rena o è un imprevisto che non si era mai verificato? Secondo me la seconda.{/color}"

    show tsumi_prop:
        ease 1 yalign 1.5
    pause 1
    hide tsumi_prop
    show hnb evilgrin fury at right onlayer overlayer
    show check fire shoutOpen fp at left onlayer overlayer
    show check at flip
    show vs_screen
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
    window hide
    with pushup
    play sound "audio/sfx/zbiin.ogg"
    show tsumi_prop:
        zoom 0.3
        xalign 0.5
        yalign - 0.4
        ease 0.7 yalign 0.0
    pause 1

    ck "FATTI SOTTO HANABI!"
    hb "FATTI SOTTO CHECK!"
    window hide


    pause 0.3

    camera:
        xalign 0.5
        yalign 0.0
        easeout_expo 1.5 zoom 3

    camera overlayer:
        easeout_expo 1.5 zoom 6

    pause 1.5

    hide check
    hide hnb

    camera:
        zoom 1
    scene tsumi_frag

    play sound "audio/sfx/doon.mp3" volume 1.5


    $renpy.transition(vpunch)
    $renpy.call_screen('welcome_tsumi')
    stop music fadeout 15
    $renpy.call_screen('welcome_tsumi')

    $ MainMenu(confirm=False)()
    return