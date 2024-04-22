

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



