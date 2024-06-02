

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
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene1_0")

            imagebutton:
                tooltip "scene2_2"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_2")

            imagebutton:
                tooltip "scene2_1"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_1")

            imagebutton:
                tooltip "scene2_0"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_0")




    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            outlines [(3, "#000")]
            xalign 0.5
            yalign 0.16
            size 40



