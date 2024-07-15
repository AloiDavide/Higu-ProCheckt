

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
screen tq_index_page(this_page, forward, backward):
    zorder 102
    modal True

    # this_page := list of titles in the current page

    # suppose I instead pass a list of page objects in here
    # TQ keeps it padded with empty objects so it always has a multiple of 14 items


    grid 2 7:
        xspacing 150
        #yspacing 70
        area (270,130,1440,860)
        for t in this_page:
            textbutton t:
                xalign 0.0
                yalign 0.5
                if t.seen:
                    text_style "handwritten_index"
                else:
                    text_style "handwritten_index_highlight"
                    #make the unread ones bold and glow dark red. on hover just change
                action [Function(TQ.get().show_question_page, t.title), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/multiple pageflips.mp3", relative_volume=2)]

    use taccuino_ui(forward=forward, backward=backward)




#----------------------------
# SPECIFIC QUESTIONS SCREEN
#----------------------------
screen tq_question_page(left, right, forward, backward):
    # left := dict - data of the left page
    # right := dict - data of the right page, or None if not present
    # forward := bool - is there a next page?
    # backward := bool - is there a previous page?
    zorder 102
    modal True


    python:
        separator_think = im.Scale("overlay/comic check think.png", 150, 150)
        separator_eureka = im.Scale("overlay/comic check eureka.png", 150, 150)

        ans_left = left['display_answer']
        ans_right = right['display_answer']

        current_page = (left["title"], right["title"])



    # left page
    vbox:
        xalign 0.2
        null height 120

        # title

        text left["title"]:
            xalign 0.5
            textalign 0.0
            xsize 600
            outlines [(0, "#000")]
            color "#000"
            size 55
            font "static/Caveat-Bold.ttf"

        null height 40

        # question
        text left["question"]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size 35
                font "static/Caveat-Regular.ttf"


        null height 20

        # separator if answer present
        if ans_left > 0:
            hbox:
                xalign 0.0
                xoffset -20
                spacing 100

                add separator_eureka

                text left["reaction"]:
                    textalign 0.5
                    yalign 0.8
                    outlines [(2, "#000")]
                    color "#6A0707"
                    size 50
                    font "static/Caveat-Regular.ttf"
        else:
            add separator_think:
                xalign 0.0
                xoffset -20


        null height 20
        # correct answer
        text left["answers"][ans_left]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size 35
                font "static/Caveat-Regular.ttf"




    # right page
    vbox:
        xalign 0.8
        null height 120
        # title
        text right["title"]:
            xalign 0.5
            textalign 0.5
            xsize 600
            outlines [(0, "#000")]
            color "#000"
            size 55
            font "static/Caveat-Bold.ttf"

        null height 40

        # question
        text right["question"]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size 35
                font "static/Caveat-Regular.ttf"

        null height 20

        # separator if answer present
        if ans_right > 0:
            hbox:
                xalign 0.0
                xoffset -20
                spacing 100

                add separator_eureka

                text right["reaction"]:
                    textalign 0.5
                    yalign 0.8
                    outlines [(2, "#000")]
                    color "#6A0707"
                    size 50
                    font "static/Caveat-Regular.ttf"
        else:
            if right["title"]!="":
                add separator_think:
                    xalign 0.0
                    xoffset -20


        null height 20
        # correct answer
        text right["answers"][ans_right]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size 35
                font "static/Caveat-Regular.ttf"


    use taccuino_ui(current_page=current_page, forward=forward, backward=backward)



#------------------------------------
#          UI BUTTONS SCREEN
#-----------------------------------

screen taccuino_ui(forward, backward, current_page=None):
    zorder 103
    python:
        bw = im.Scale("overlay/bw.png", 70, 40)
        fw = im.Scale("overlay/fw.png", 70, 40)
        bw_h = im.Scale("overlay/bw_h.png", 70, 40)
        fw_h = im.Scale("overlay/fw_h.png", 70, 40)

        colors = ["black", "red", "green", "blue"]
        bookmarks = ["overlay/"+color+" bookmark.png" for color in colors]
        bookmarks_hover = ["overlay/"+color+" bookmark ext.png" for color in colors]

    # Topic Bookmarks
    vbox:
        xsize 200
        xalign 0.122
        yalign 0.1
        spacing 20

        for i in range(4):
            imagebutton:
                idle bookmarks[i]
                hover bookmarks_hover[i]
                hover_xoffset 5
                action [Function(Taccuino.tq().show_index_page,0,i), With(Pixellate(0.6,3)), Play("sound", "audio/sfx/multiple pageflips.mp3", relative_volume=2)]


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
    imagebutton:
            xalign 0.01
            yalign 0.01
            idle im.Scale("overlay/notes_icon.png", 50, 50)
            hover im.Scale("overlay/notes_icon.png", 100, 100)
            hover_sound "audio/sfx/pageflip.mp3"
            activate_sound "audio/sfx/multiple pageflips.mp3"
            action [Function(hide_notebook), With(easeoutbottom)]

