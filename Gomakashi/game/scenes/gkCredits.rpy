screen credits(scroll_duration):
    $credits_chorusA = """C' era un detective assai altisonante
Dal tono di voce molto squillante
Con fibra morale assai resistente
Eppure, il cervello, ahimè, latitante
"""

    $credits_chorusB = """Finì intrappolato in un gioco dannato
Un gioco impossibile, un gioco truccato
Un gioco che cela una vile tortura
Che ne era in realtà lo scopo celato
"""

    $credits_verseA = """La strega giocando col suo bel pupazzo, dai capelli blu e la figura sottile
Lo stringe, lo lancia, lo strappa in due parti, eppure, mistero, si rialza ogni volta
Finche tutto a un tratto, decenni e più dopo, si desta e si inchina con fare civile
Le parla e la fissa con grande sarcasmo, che sfidi la strega? Che folle! Che stolta!
"""
    $credits_verseB = """
La donzella blu è in decisivo svantaggio, decide "non posso combatter da sola"
Agguanta un detective da dentro un frammento, gli dice "Messere ho bisogno di aiuto"
Il povero uomo con gran diligenza decide di dar la sua ferma parola
Ma tutto l' impegno di quel vasto mare non riesce a celar che no, non è astuto
"""
    $credits_verseC = """
La strega curiosa appoggia il suo sguardo sul tristo detective ormai in alto mare
"Ma questo è un affronto alquanto sgarbato, lei ha un sottoposto ed io non ne ho alcuno?"
Decide, abbisogna di un degno compagno, che subito si appresta a resuscitare
Un uomo dannato, un uomo finito, dal tristo destino, terribile e bruno
"""
    $credits_verseD = """
Processo, sentenza, sia dunque un duello!, Agente scadente e soldato spietato
Che c'è poi da dire, qualcuno è sorpreso? in quale altro modo poteva finire?
Sconfitta schiacciante, sconfitta esemplare, cioè il risultato atteso e scontato.
Si chiede il detective che attende la fine, è questo il destino che devo soffrire?
"""

    $credits_epilogueA = """
Ben prima del tutto, una povera bimba, richiede alla strega dal giallo colore
"Vorrei che i miei sforzi abbian certo successo" La strega negli occhi ha un vivace brio
"Qual è il tuo obiettivo" lei chiede, cercando una tregua da noia, ozio e tepore
Un ghigno le appare nel volto alla folle risposta. "Diventerò un Dio."
"""

    $credits_epilogueB = """
Il principio di tutto fu una povera bimba, per cui una strega provò simpatia
"Vorrei la certezza che con i miei sforzi io possa renderere il destino mio."
"Qual è il tuo obiettivo?" le chiese la strega, cercando una tregua dalla monotonia
Un ghigno seguì la sua folle risposta. "La mia ambizione è essere un Dio."
"""


    python:
        separator = im.FactorScale("overlay/credits_separator.png", 0.70)

        roles = {
            "CONCEPT" : ["Crunter", "HounDogs"],
            "SCRITTURA" : ["Crunter", "HounDogs"],
            "REGIA" : ["Crunter", "HounDogs"],
            "IMPLEMENTAZIONE" : ["HounDogs"],
            "REVISIONI" : ["Crunter"],
            "CHARACTER DESIGN" : ["Alice"],
            "ASSET ORIGINALI" : ["Alice"],
            "ASSET NON ORIGINALI" : ["07th expansion"],
            "ADATTAMENTO ASSET" : ["HounDogs"],
            "GAME ENGINE" : ["Ren'Py"],
            "STORIA ORIGINALE" : ["Ryuukishi07"],
            "ISPIRAZIONE" : ["Check", "Hanabi"],
            "DETECTIVE" : ["Check"]
        }


    vbox xalign 0.5 spacing 10:


        null height 100

        add separator:
            xalign 0.5

        textbutton credits_chorusA:
            xalign 0.5
            text_style "credits_green"

        textbutton credits_chorusB:
            xalign 0.5
            text_style "credits_orange"

        add separator:
            xalign 0.5

        textbutton credits_verseA:
            xalign 0.5
            text_style "credits_green"

        textbutton credits_verseB:
            xalign 0.5
            text_style "credits_orange"

        textbutton credits_verseC:
            xalign 0.5
            text_style "credits_green"

        textbutton credits_verseD:
            xalign 0.5
            text_style "credits_orange"

        add separator:
            xalign 0.5

        textbutton credits_chorusA:
            xalign 0.5
            text_style "credits_orange"

        textbutton credits_chorusB:
            xalign 0.5
            text_style "credits_green"

        add separator:
            xalign 0.5

        textbutton "~ La strega di boh":
            xalign 1.0
            text_style "credits_orange"

        textbutton "~ La strega di boh":
            xalign 1.0
            text_style "credits_green"

        null height 320

        add "gui/HiguLogo.png":
            xalign 0.5

        text "{color=#E29F00}HounDogs{/color} and {color=#00D915}Crunter{/color} present. Welcome to Hinamizawa...":
            outlines [(5, "#000")]
            size 30
            xalign 0.55
            font "static/POORICH.TTF"

        text "Gli indizi perduti.":
            outlines [(5, "#000")]
            size 30
            xalign 0.73
            font "static/POORICH.TTF"

        for role in roles:
            hbox xalign 0.6 spacing 150 xsize 700:

                text role:
                    xalign 0.5
                    textalign 0.5
                    size 30
                    font "static/Caveat-Regular.ttf"


                vbox:
                    xalign 1.0
                    for person in roles[role]:
                        text person:
                            xalign 0.5
                            textalign 0.5
                            size 30
                            font "static/Caveat-Regular.ttf"

            null height 50

        add separator:
            xalign 0.5

        textbutton credits_epilogueA:
            xalign 0.5
            text_style "credits_normal"

        add separator:
            xalign 0.5


label credits_scene:
    call hide_menu
    "Check is dead, slowly fade to black"

    camera:
        zoom 1.01
        xalign 0.5

    scene credits_background with fade
#     scene vortex with fade

#     play music "audio/umi/fighy aroma.mp3"
#     play music "audio/umi/black liliana.mp3" # the best
#     play music "audio/umi/happy maria.mp3" # the best for poem
#     play music "audio/umi/melody.mp3"
    play music "audio/umi/bring the fate.mp3" volume 1.3

# Happy maria coming from Lambdadelta doing her final taunt
# Into black liliana when the credits credit
# Black liliana swella nel momento in cui esce l'ultima poesia

#     $renpy.show_screen("credits", credits_script, _layer="overlayer")


    $scroll_duration = 300
    $stop_point = -5*1080 -800
    #circa 300

    $ persistent.notes = False
    $ quick_menu = False
    $ _skipping = False

    show screen credits(scroll_duration) onlayer overlayer

    #scroll credits
    camera overlayer:
        ypos 1080
        linear scroll_duration ypos stop_point


    $renpy.pause(scroll_duration, hard=True)

    "STOP CREDITS"
    window hide

    $ persistent.notes = True
    $ quick_menu = True
    $ _skipping = True

    camera overlayer:
        yalign 0.5
        xalign 0.5
    hide credits onlayer overlayer

    show screen fine onlayer overlayer with dissolve

    pause


    hide screen fine onlayer overlayer
    play sound "audio/sfx/laugh.mp3"
    show screen fine2 onlayer overlayer
    with squares

    pause 2




    camera overlayer:
        zoom 1
        easeout_expo 2.5 zoom 400

    pause 2
    hide screen fine2 onlayer overlayer



    show meakashi_prop onlayer overlayer:
        align (0.5, 0.5)
        zoom 0.0025
        easeout_expo 3.5 zoom 3.5

    pause 3

    scene hinamizawa onlayer overlayer
    camera overlayer:
        zoom 1

    with Dissolve(1.5)

    jump gk301



    return


screen fine:
    text "FINE DEL GIOCO":
        xalign 0.5
        yalign 0.5
        textalign 0.5
        size 60
        font "static/Caveat-SemiBold.ttf"

screen fine2:
    text "FINE DEL GIOCO.......?":
        xalign 0.5
        yalign 0.5
        textalign 0.5
        size 60
        font "static/Caveat-SemiBold.ttf"