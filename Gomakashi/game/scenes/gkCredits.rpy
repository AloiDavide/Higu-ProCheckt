screen credits():
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

    $credits_verse = """La strega giocando col suo bel pupazzo, dai capelli blu e la figura sottile
Lo stringe, lo lancia, lo strappa in due parti, eppure, mistero, si rialza ogni volta
Finche tutto a un tratto, decenni e più dopo, si desta e si inchina con fare civile
Le parla e la fissa con grande sarcasmo, che sfidi la strega? Che folle! Che stolta!

La donzella blu è in decisivo svantaggio, decide "non posso combatter da sola"
Agguanta un detective da dentro un frammento, gli dice "Messere ho bisogno di aiuto"
Il povero uomo con gran diligenza decide di dar la sua ferma parola
Ma tutto l' impegno di quel vasto mare non riesce a celar che no, non è astuto

La strega curiosa appoggia il suo sguardo sul tristo detective ormai in alto mare
"Ma questo è un affronto alquanto sgarbato, lei ha un sottoposto ed io non ne ho alcuno?"
Decide, abbisogna di un degno compagno, che subito si appresta a resuscitare
Un uomo dannato, un uomo finito, dal tristo destino, terribile e bruno

Processo, sentenza, sia dunque un duello!, Agente scadente e soldato spietato
Che c'è poi da dire, qualcuno è sorpreso? in quale altro modo poteva finire?
Sconfitta schiacciante, sconfitta esemplare, cioè il risultato atteso e scontato.
Si chiede il detective che attende la fine, è questo il destino che devo soffrire?
"""

    python:
        separator = "overlay/credits_separator.png"

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
            "STREGHE" : ["Crunter", "HounDogs"],
            "DETECTIVE" : ["Check"]
        }



    vbox xalign 0.5 spacing 10:




        textbutton credits_chorusA:
            xalign 0.5
            text_style "credits_green"

        textbutton credits_chorusB:
            xalign 0.5
            text_style "credits_orange"

        add separator:
            xalign 0.5

        textbutton credits_verse:
            xalign 0.5
            text_style "credits_green"

        add separator:
            xalign 0.5

        textbutton credits_chorusA:
            xalign 0.5
            text_style "credits_orange"

        textbutton credits_chorusB:
            xalign 0.5
            text_style "credits_green"

        null height 400

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

        null height 100
        text "FINE...":
            xalign 0.5
            textalign 0.5
            size 60
            font "static/Caveat-Regular.ttf"



label credits_scene:
    call hide_menu
    "Check is dead, slowly fade to black"

    camera:
        zoom 1.01
        xalign 0.5

    scene credits_background with fade
#     scene vortex with fade



    play music "audio/umi/black liliana.mp3"


#     $renpy.show_screen("credits", credits_script, _layer="overlayer")
    show screen credits onlayer overlayer

    $scroll_duration = 230

    camera overlayer:
        ypos 1080
        linear scroll_duration ypos -5*1080

    $ _skipping = False
    $renpy.pause(scroll_duration, hard=True)

    hide screen credits
    $ _skipping = True
    "STOP CREDITS"

    return
