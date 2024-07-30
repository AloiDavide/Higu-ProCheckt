

#screen button_string(title):
#    text title:
#        outlines [(3, "#000")]
#        xalign 0.5
#        yalign 0.2
#        size 40

default persistent.first = False
default persistent.second = False
default persistent.third = False


screen tips():
    python:
        damA = im.Scale("thumbnails/damA.png", 360, 225)
        dam_overB = im.Scale("thumbnails/dam_overB.png", 360, 225)

        t20a = im.Scale("thumbnails/2.0.a.png", 360, 225)
        t20b = im.Scale("thumbnails/2.0.b.png", 360, 225)
        t21a = im.Scale("thumbnails/2.1.a.png", 360, 225)
        t21b = im.Scale("thumbnails/2.1.b.png", 360, 225)
        t22a = im.Scale("thumbnails/2.2.a.png", 360, 225)
        t22b = im.Scale("thumbnails/2.2.b.png", 360, 225)

        #persistent._clear()

    #312, 195
    #336, 210
    #360, 225
    $view = str(persistent.first)+" "+str(persistent.second)+" "+str(persistent.third)
    label view:
            xalign 0.5
            yalign 0.1

    if persistent.first and persistent.second and persistent.third:


        imagebutton:
                xalign 1.0
                tooltip "Metodo Socratico"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_1_X")
    else:
        label "no extras":
            xalign 0.5




    hbox xalign 0.5 yalign 0.7 spacing 100:

        vbox xalign 0.5 yalign 0.5 spacing 30:

            imagebutton:
                tooltip "Metodo Socratico"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Call("scene1_0")

        null width 100

        vbox xalign 0.5 yalign 0.5 spacing 30:
            imagebutton:
                tooltip "scene2_2"
                idle t22a
                hover t22b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Call("scene2_2")

            imagebutton:
                tooltip "scene2_1"
                idle t21a
                hover t21b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Call("scene2_1")

            imagebutton:
                tooltip "scene2_0"
                idle t20a
                hover t20b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Call("scene2_0")





    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            outlines [(4, "#000")]
            xalign 0.5
            yalign 0.16
            size 60
            font "static/yuminl.ttf"



