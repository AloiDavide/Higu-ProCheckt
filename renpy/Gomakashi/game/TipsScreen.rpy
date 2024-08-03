

#screen button_string(title):
#    text title:
#        outlines [(3, "#000")]
#        xalign 0.5
#        yalign 0.2
#        size 40

default persistent.first = False
default persistent.second = False
default persistent.third = False
default persistent.notes = False

screen curtains():
    frame:
        mousearea:
            area (0,0,1920, 1080)

screen prism():
    zorder 4
    python:
        rainbow = "overlay/rainbow.png"
        white_beam = "overlay/white_beam.png"
        rainbow_reverse = "overlay/rainbow.png"
    if True:
        add rainbow:
            pos (478,340)

        add white_beam:
            pos (-60,580)

#         add rainbow_reverse:
#             pos (1136,340)
#             xzoom -1

screen secret():
    python:
        cut = "overlay/cut.png"
    imagebutton:
        xalign 1.0
        idle cut
        hover cut
        focus_mask cut
        hover_sound "audio/sfx/darkso cursor.mp3"
        activate_sound "audio/sfx/stone slide magic.mp3"
        action Jump("scene2_X")


screen tips():
    zorder 5
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






    hbox xalign 0.13 yalign 0.7 spacing 300:

        vbox yalign 0.5 spacing 30:

            imagebutton:
                tooltip "Metodo Socratico"
                idle damA
                hover dam_overB
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene1_0")



        vbox yalign 0.5 spacing 30:
            imagebutton:
                tooltip "Scacco Matto."
                idle t22a
                hover t22b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_2")



            imagebutton:
                tooltip "Il Demone e l'Assistente."
                idle t20a
                hover t20b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_0")

            imagebutton:
                tooltip "Condanna."
                idle t21a
                hover t21b
                hover_sound "audio/sfx/darkso cursor.mp3"
                activate_sound "audio/sfx/stone slide magic.mp3"
                action Jump("scene2_1")



#         vbox yalign 0.5 spacing 30:
#             imagebutton:
#                 tooltip "Metodo Socratico"
#                 idle damA
#                 hover dam_overB
#                 hover_sound "audio/sfx/darkso cursor.mp3"
#                 activate_sound "audio/sfx/stone slide magic.mp3"
#                 action Call("scene1_0")



    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            outlines [(4, "#000")]
            xalign 0.5
            yalign 0.16
            size 60
            font "static/yuminl.ttf"



