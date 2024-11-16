
#screen button_string(title):
#    text title:
#        outlines [(3, "#000")]
#        xalign 0.5
#        yalign 0.2
#        size 40

screen tips():
    $w = 360
    $h = 225
    $closed1 = im.Scale("notes closed border.png", w, h)
    $open1 = im.Scale("notes border.png", w, h)
    $closed2 = im.Scale("news border.png", w, h)
    $open2 = im.Scale("news more border.png", w, h)
    $closed3 = im.Scale("hinamizawa border.png", w, h)
    $open3 = im.Scale("clinic out border.png", w, h)
    $closed4 = im.Scale("koya border.png", w, h)
    $open4 = im.Scale("basement border.png", w, h)
    $closed5 = im.Scale("satokhome border.png", w, h)
    $open5 = im.Scale("satokhome sunset border.png", w, h)
    $closed6 = im.Scale("shrine night border.png", w, h)
    $open6 = im.Scale("red border.png", w, h)
    $closed7 = im.Scale("red border.png", w, h)
    $open7 = im.Scale("red frag border.png", w, h)
    $closed8 = im.Scale("woods1 border.png", w, h)
    $open8 = im.Scale("moon border.png", w, h)
    $closed9 = im.Scale("telephone border.png", w, h)
    $open9 = im.Scale("notes closed border.png", w, h)
    #312, 195
    #336, 210
    #360, 225





    vbox xalign 0.5 yalign 0.7 spacing 30:

        hbox xalign 0.5 yalign 0.5 spacing 30:
#             imagebutton:
#                 tooltip "Welcome To Hinamizawa 3"
#                 idle closed1
#                 hover open1
#                 action Jump("wth3")

            imagebutton:
                tooltip "Taccuino Investigazioni"
                idle closed1
                hover open1
                action Jump("tip1")

            imagebutton:
                tooltip "Verbale Archiviazione Caso"
                idle closed2
                hover open2
                action Jump("tip2")

            imagebutton:
                tooltip "Due Bizzarri Pazienti"
                idle closed3
                hover open3
                action Jump("tip3")


        hbox xalign 0.5 yalign 0.5 spacing 30:


            imagebutton:
                tooltip "Libero Arbitrio"
                idle closed4
                hover open4
                action Jump("tip4")

            imagebutton:
                tooltip "Destituzione"
                idle closed5
                hover open5
                action Jump("tip5")

            imagebutton:
                tooltip "Territorio Divino"
                idle closed6
                hover open6
                action Jump("tip6")




        hbox xalign 0.5 yalign 0.5 spacing 30:
            imagebutton:
                tooltip "Nuova Regola"
                idle closed7
                hover open7
                action Jump("tip7")

            imagebutton:
                tooltip "Ultima Volta"
                idle closed8
                hover open8
                action Jump("tip8")

            imagebutton:
                tooltip "Verità"
                idle closed9
                hover open9
                action Jump("tip9")


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
    $default = im.Scale("choice fragment.png",w,h)
    $hovering = im.Scale("choice fragment hover.png",w,h)



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

