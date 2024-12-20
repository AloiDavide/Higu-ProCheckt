
#-----------------------------------------------------------------
#Backdrop with the notebook image
screen taccuino():
    zorder 101
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)

    frame:
        add taccuino_overlay


#----------------------------
#     INDEX PAGE SCREEN
#----------------------------
screen tq_index_page(titles, forward, backward, pb):
    zorder 102
    modal True

    # this_page := list of titles in the current page

    # suppose I instead pass a list of page objects in here
    # TQ keeps it padded with empty objects so it always has a multiple of 14 items
    $important = Transform("overlay/important.png", offset=(0,0), align=(0.5,0.5))
    vpgrid:
        scrollbars "vertical"
        vscrollbar_unscrollable "hide"
        cols 2
        rows 7
        area (150,130,1840,960)
        for t in titles:
            textbutton t[0]:
                if not t[1]:
                    background important
                xsize 800
                ysize 130
                xalign 0.0
                yalign 0.5
                text_style "handwritten_index"
                action [Function(Taccuino.tq().show_question_page, t[0]), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/multiple pageflips.mp3", relative_volume=2)]


#     grid 2 7:
#
#         xspacing 150
#         #yspacing 70
#         area (270,130,1440,860)
#         for t in this_page:
#             textbutton t:
#                 xalign 0.0
#                 yalign 0.5
#                 text_style "handwritten_index"
#                 action [Function(Taccuino.tq().show_question_page, t), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/multiple pageflips.mp3", relative_volume=2)]

    use taccuino_ui(forward=forward, backward=backward, stay=pb, isIndex=True)




#----------------------------
# SPECIFIC QUESTIONS SCREEN
#----------------------------
screen tq_question_page(left, right, forward, backward):
    zorder 102
    modal True

    use tq_question(left, 0.2)

    use tq_question(right, 0.8)

    $ current_page = (left["title"], right["title"])
    use taccuino_ui(current_page=current_page, forward=forward, backward=backward)


screen tq_question(page, position):
    zorder 103
    modal True


    $separator_think = im.Scale("overlay/comic check think.png", 150, 150)
    $separator_eureka = im.Scale("overlay/comic check eureka.png", 150, 150)
#     $tsize = page.get_tsize()

    python:
        import math

        text_length = len(page['question']) + len(page["answers"][page["display_answer"]])

        shrink_factor = 18
        shrink_limit = 550

        shrink = max(0, math.ceil((text_length - shrink_limit) / shrink_factor))

        tsize= 35 - shrink


    vbox:
        xalign position
        null height 120

        # title

        text page["title"]:
            xalign 0.5
            textalign 0.0
            xsize 600
            outlines [(0, "#000")]
            color "#000"
            size 55
            font "static/Caveat-Bold.ttf"

        null height 40

        # question
        text page["question"]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size tsize
                font "static/Caveat-Regular.ttf"


        null height 20

        # separator if answer present
        if page["display_answer"] > 0:
            hbox:
                xalign 0.0
                xoffset -20
                spacing 100

                add separator_eureka

                text page["reaction"]:
                    textalign 0.5
                    yalign 0.8
                    outlines [(2, "#000")]
                    color "#8A0707"
                    size 50
                    font "static/Caveat-Regular.ttf"
        else:
            if page["title"]!="":
                add separator_think:
                    xalign 0.0
                    xoffset -20

        null height 20

        # correct answer
        text page["answers"][page["display_answer"]]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size tsize
                font "static/Caveat-Regular.ttf"


#------------------------------------
#          UI BUTTONS SCREEN
#-----------------------------------

screen taccuino_ui(forward, backward, current_page=None, stay=False, isIndex=False):
    zorder 103
    python:
        bw = im.Scale("overlay/bw.png", 70, 40)
        fw = im.Scale("overlay/fw.png", 70, 40)
        bw_h = im.Scale("overlay/bw_h.png", 70, 40)
        fw_h = im.Scale("overlay/fw_h.png", 70, 40)

        colors = ["black", "red", "green", "blue"]
        bookmarks = ["overlay/"+color+" bookmark.png" for color in colors]
        bookmarks_hover = ["overlay/"+color+" bookmark ext.png" for color in colors]

        topic = Taccuino.tq().current_topic



    # Topic Bookmarks
    if topic > 0 and isIndex:
            mousearea:
                area (0.11, 0.05, 0.3, 0.45)
                hovered [Function(Taccuino.tq().show_index_page, None, None, False), Show("help")]
                unhovered [Function(Taccuino.tq().show_index_page, None, None, True), Hide("help")]

    vbox:
        xsize 200
        xalign 0.122
        yalign 0.1
        spacing 20

        for i in range(4):
            imagebutton:
                if stay and i==topic:
                    idle bookmarks_hover[i]
                else:
                    idle bookmarks[i]
                    hover bookmarks_hover[i]

                    action [Function(Taccuino.tq().show_index_page,0,i, topic==0), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/multiple pageflips.mp3", relative_volume=2)]


    # Page Turn

    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.95
            idle fw
            hover fw_h

            if current_page is not None:
                action [Function(Taccuino.tq().turn_question_page, True, current_page), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/pageflip.mp3")]
            else:
                action [Function(Taccuino.tq().turn_index_page, True), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/pageflip.mp3")]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.95
            idle bw
            hover bw_h

            if current_page is not None:
                action [Function(Taccuino.tq().turn_question_page, False, current_page), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/pageflip.mp3")]
            else:
                action [Function(Taccuino.tq().turn_index_page, False), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/pageflip.mp3")]

    # Exit Button
    python:
        if Taccuino.tq().hasNew():
            icon = "overlay/notes_icon_active.png"
        else:
            icon = "overlay/notes_icon.png"

    if persistent.notes:
        imagebutton:
            xalign 0.01
            yalign 0.01
            idle im.Scale(icon, 50, 50)
            hover im.Scale(icon, 100, 100)
            hover_sound "audio/sfx/pageflip.mp3"
            activate_sound "audio/sfx/multiple pageflips.mp3"
            action [Function(hide_notebook)]

screen help:
    #marker of whn I enter the textarea
    zorder 104
    label "":
        xalign 0.5