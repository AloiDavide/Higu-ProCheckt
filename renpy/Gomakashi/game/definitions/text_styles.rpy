init:
    style wide is text:
            size 35
            xpos 367
            ypos 60

            ymaximum 1000
            textalign 0.0
            xmaximum 1200
            outlines [(2, "#000", 1,1)]

    style codec is text:
            size 35
            xpos 367
            ypos -170

            ymaximum 1000
            textalign 0.0
            xmaximum 1200
            outlines [(2, "#000", 1,1)]

    style notes_dialogue is text:
            size 35
            xpos 367
            ypos 60

            ymaximum 1000
            textalign 0.0
            xmaximum 1200
            outlines [(2, "#000", 1,1)]
            font "static/Caveat-Regular.ttf"

    style beach_text is text:
            size 45
            xpos 180
            ypos 60

            ymaximum 1000
            textalign 0.0
            xmaximum 1200
            outlines [(4, "#000", 1,1)]
            font "static/Caveat-Regular.ttf"

    style wideN is text:
            size 35
            xpos 367
            ypos 50

            ymaximum 1000
            textalign 0.0
            xmaximum 1200
            outlines [(2, "#000", 1,1)]

    style border is text:
        size 45
        outlines [(2, "#000", 1, 1)]

    style white_border is text:
        size 45
        outlines [(2, "#fff", 1, 1)]


    style handwritten_index:
        outlines [(0, "#000")]
        hover_outlines [(2, "#000")]
        color "#000"
        hover_color "#8A0707"
        size 45
        textalign 0.5
        font "static/Caveat-Regular.ttf"

    style menu_text:
        outlines [(1, "#000")]
        hover_outlines [(2, "#000")]
        hover_bold True
        align (0.5, 0.5)
        size 40
        color "009015"
        hover_color "#00D915"

    style menu_buttons:
        background "overlay/menu_button.png"
        hover_background im.Flip("overlay/menu_button_hover.png", horizontal=True, vertical=True)
        align (0.5,0.5)

        xsize 528 ysize 72