

#screen button_string(title):
#    text title:
#        outlines [(3, "#000")]
#        xalign 0.5
#        yalign 0.2
#        size 40



screen tips():
    $courtroom_B = im.Scale("thumbnails/courtroom B.jpg", 360, 225)
    $bern_kekkai_B = im.Scale("thumbnails/bern kekkai B.png", 360, 225)
    $fragplane_A = im.Scale("thumbnails/fragplane A.png", 360, 225)
    $vortex_A = im.Scale("thumbnails/vortex A.png", 360, 225)
    $vortex_B = im.Scale("thumbnails/vortex B.png", 360, 225)
    $small_shrine_A = im.Scale("thumbnails/small shrine A.png", 360, 225)
    $small_shrine_over_B = im.Scale("thumbnails/small shrine over B.png", 360, 225)


    #312, 195
    #336, 210
    #360, 225


    vbox xalign 0.5 yalign 0.5 spacing 30:

        hbox xalign 0.5 yalign 0.5 spacing 30:
            #imagebutton:
            #    tooltip "Welcome To Hinamizawa 3"
            #    idle bern_kekkai
            #    hover bern_kekkai
            #    action Jump("wth3")

            imagebutton:
                tooltip "Le luci nel cielo sono frammenti"
                idle fragplane_A
                hover bern_kekkai_B
                action Jump("wth4")

            imagebutton:
                tooltip "Nascita di una pedina"
                idle vortex_A
                hover vortex_B
                action Jump("wthnb")
            imagebutton:
                tooltip "CHECK fuori da Check"
                idle small_shrine_A
                hover small_shrine_over_B
                action Jump("intermissionA")

        hbox xalign 0.5 yalign 0.5 spacing 30:
            imagebutton:
                tooltip "Turnabout Witch"
                idle bern_kekkai_B
                hover courtroom_B
                action Jump("returnal")



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