

#screen button_string(title):
#    text title:
#        outlines [(3, "#000")]
#        xalign 0.5
#        yalign 0.2
#        size 40



screen tips():
    $bern_kekkai_B = im.Scale("thumbnails/bern kekkai B.png", 360, 225)
    $fragplane_A = im.Scale("thumbnails/fragplane A.png", 360, 225)
    $damA = im.Scale("thumbnails/damA.png", 360, 225)
    $dam_overB = im.Scale("thumbnails/dam_overB.png", 360, 225)


    #312, 195
    #336, 210
    #360, 225


    vbox xalign 0.5 yalign 0.5 spacing 30:

        hbox xalign 0.5 yalign 0.5 spacing 30:

            imagebutton:
                tooltip "Metodo Socratico"
                idle damA
                hover dam_overB
                action Jump("chessboard0")

#            imagebutton:
#                tooltip "Jump to layer 1"
#                idle fragplane_A
#                hover bern_kekkai_B
#                action Jump("chessboard1")
#
#            imagebutton:
#                tooltip "Jump to layer 2"
#                idle fragplane_A
#                hover bern_kekkai_B
#                action Jump("chessboard2")






    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            outlines [(3, "#000")]
            xalign 0.5
            yalign 0.16
            size 40











style choice is text:
        color "#0000cf"
        outlines [(1, "#111", 1,1)]
        xalign 0.5
        yalign 0.5


screen fragment_choice():
    $w = 900
    $h = 300
    $default = im.Scale("overlay/choice fragment.png",w,h)
    $hovering = im.Scale("overlay/choice fragment hover.png",w,h)



    vbox xalign 0.5 yalign 0.5 spacing 200:

        textbutton "{i}Ostacola Keiichi nell'omicidio.{/i}":
            background default
            hover_background hovering
            text_style "choice"
            #text_xalign 0.5
            xysize (w, h)

            action Jump("tip4P")

        textbutton "Aiuta Keiichi nell'omicidio.":
            background default
            hover_background hovering
            text_style "choice"
            xysize (w, h)
            action Jump("tip4G")

screen welcome_hima():
    vbox xalign 0.5 yalign 0.5 spacing 50:
        add "overlay/welcome.png"

        text "Ch.4 Himatsubushi":
            outlines [(3, "#101010")]
            size 100
            color "#0000cf"
            xalign 0.5
            font "static/yuminl.ttf"

    timer 15.0 action Return()

screen welcome_meakashi():
    vbox xalign 0.5 yalign 0.5 spacing 50:
        add "overlay/welcome.png"

        text "Ch.5 Meakashi":
            outlines [(3, "#101010")]
            size 100
            color "#23c076"
            xalign 0.5
            font "static/yuminl.ttf"

    timer 15.0 action Return()

screen rule1():
    text "Da ora in poi Bernkastel e Check non si possono scambiare informazioni inerenti alla partita.":
            outlines [(2, "#101010")]
            size 40
            color "#ffe674"
            xalign 0.5
            yalign 0.5
            font "static/yuminl.ttf"

screen rule2():
    text "Check non può riconoscere la mia pedina..":
            outlines [(2, "#101010")]
            size 40
            color "#ffe674"
            xalign 0.5
            yalign 0.5
            font "static/yuminl.ttf"