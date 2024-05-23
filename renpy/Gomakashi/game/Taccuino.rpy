init python:
    import json

    showing_notes = False

    def show_notebook():
        renpy.show_screen("taccuino")
        Taccuino.tq().show_index_page()

        global showing_notes
        showing_notes = True


    def hide_notebook():
        renpy.hide_screen("taccuino")
        renpy.hide_screen("tq_index_page")
        renpy.hide_screen("tq_question_page")


        global showing_notes
        showing_notes = False

    # updates the seen flag in the json to true for both entries in the page tuple
    def set_as_seen(page):
        pass

    def pad_titles(titles, per_page):
        res = titles
        while len(res) % per_page != 0:
                res = res + [""]
        return res

    def pair_titles(titles):
        return [(titles[i], titles[i + 1] if i + 1 < len(titles) else "") for i in range(0, len(titles), 2)]


    class Taccuino:
        instance = None

        def __init__(self):
            self.per_page = 14
            self.index_page = 0
            self.current_topic = 0 #MAKE THIS AN ENUM

            self.tq_data = {}
            self.titles = []

            with renpy.open_file("notes.json") as file:
                self.tq_data = json.load(file)


            self.titles = [page_data['title'] for page_data in self.tq_data["0"].values()]



        #Signleton
        @staticmethod
        def tq():
            if Taccuino.instance is None:
                Taccuino.instance = Taccuino()

            return Taccuino.instance

        #calls the index screen
        def show_index_page(self, page = None, topic=None):
            if page is None:
                page = self.index_page
            else:
                self.index_page = page
            if topic is None:
                topic = self.current_topic
            else:
                self.current_topic = topic

            self.titles = list(self.tq_data[str(topic)].keys())

            padded_titles = pad_titles(self.titles, self.per_page)

            bw = False if page == 0 else True
            fw = False if (page+1)*self.per_page == len(padded_titles) else True


            this_page = padded_titles[page*self.per_page:(page+1) * self.per_page]


            renpy.hide_screen("tq_question_page")
            renpy.show_screen("tq_index_page", this_page=this_page, forward=fw, backward=bw)


        def turn_index_page(self, forward: bool):
            self.index_page = self.index_page+1 if forward else self.index_page-1
            self.show_index_page()

        def show_question_page(self, title):
            print("Showing specific page for:\n" + title)

            paired_titles = pair_titles(self.titles)


            page = ()
            for pair in paired_titles:
                if title in pair: page = pair

            set_as_seen(page)

            bw = False if page == paired_titles[0] else True
            fw = False if page == paired_titles[-1] else True

            topic = str(self.current_topic)
            left = self.tq_data[topic][page[0]]
            right = self.tq_data[topic][page[1]]

            renpy.hide_screen("tq_index_page")
            renpy.show_screen("tq_question_page", left=left, right=right, forward=fw, backward=bw)
            
        def turn_question_page(self, forward: bool, page):
            paired_titles = pair_titles(self.titles)

            current = paired_titles.index(page)
            next = current + 1 if forward else current - 1

            self.show_question_page(paired_titles[next][0])








#-----------------------------------------------------------------
screen black():
    $black = im.Scale("bg/black.jpg", 1920, 1080)
    zorder 100
    frame:
        null
    #add black

screen taccuino():
    zorder 101
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)


    frame:
        add taccuino_overlay




# tq : Taccuino object
screen tq_index_page(this_page, forward, backward):
    zorder 102
    modal True
    # this_page := list of titles in the current page


    python:
        bw = im.Scale("overlay/bw.png", 70, 40)
        fw = im.Scale("overlay/fw.png", 70, 40)
        bw_h = im.Scale("overlay/bw_h.png", 70, 40)
        fw_h = im.Scale("overlay/fw_h.png", 70, 40)

        black_bm = "overlay/black bookmark.png"
        black_bm_ext = "overlay/black bookmark ext.png"

        red_bm = "overlay/red bookmark.png"
        red_bm_ext = "overlay/red bookmark ext.png"

        green_bm = "overlay/green bookmark.png"
        green_bm_ext = "overlay/green bookmark ext.png"

        blue_bm = "overlay/blue bookmark.png"
        blue_bm_ext = "overlay/blue bookmark ext.png"



    grid 2 7:
        xspacing 150
        #yspacing 70
        area (270,130,1440,860)
        for t in this_page:
            textbutton t:
                xalign 0.0
                yalign 0.5
                text_style "handwritten_index"
                action [Function(Taccuino.tq().show_question_page, t), With(Pixellate(0.6,3))]


    # Topic Bookmarks
    vbox:
        xsize 200
        xalign 0.122
        yalign 0.1
        spacing 20

        imagebutton:
            idle black_bm
            hover black_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,0), With(Pixellate(0.6,3))]

        imagebutton:
            idle red_bm
            hover red_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,1), With(Pixellate(0.6,3))]

        imagebutton:
            idle green_bm
            hover green_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,2), With(Pixellate(0.6,3))]

        imagebutton:
            idle blue_bm
            hover blue_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,3), With(Pixellate(0.6,3))]

    # Page Turn

    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.95
            idle fw
            hover fw_h


            action [Function(Taccuino.tq().turn_index_page, True), With(Pixellate(0.6,3))]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.95
            idle bw
            hover bw_h
            action [Function(Taccuino.tq().turn_index_page, False), With(Pixellate(0.6,3))]

    # Exit Button
    imagebutton:
            xalign 0.01
            yalign 0.01
            idle im.Scale("overlay/notes_icon.png", 50, 50)
            hover im.Scale("overlay/notes_icon.png", 100, 100)
            action [Function(hide_notebook), With(easeoutbottom)]



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

    # Page flip buttons
    python:
        bw = im.Scale("overlay/bw.png", 70, 40)
        fw = im.Scale("overlay/fw.png", 70, 40)
        bw_h = im.Scale("overlay/bw_h.png", 70, 40)
        fw_h = im.Scale("overlay/fw_h.png", 70, 40)

        green_bm = "overlay/green bookmark.png"

        separator_think = im.Scale("overlay/comic check think.png", 150, 150)
        separator_eureka = im.Scale("overlay/comic check eureka.png", 150, 150)

        ans_left = left['display_answer']
        ans_right = right['display_answer']



        black_bm = "overlay/black bookmark.png"
        black_bm_ext = "overlay/black bookmark ext.png"

        red_bm = "overlay/red bookmark.png"
        red_bm_ext = "overlay/red bookmark ext.png"

        green_bm = "overlay/green bookmark.png"
        green_bm_ext = "overlay/green bookmark ext.png"

        blue_bm = "overlay/blue bookmark.png"
        blue_bm_ext = "overlay/blue bookmark ext.png"




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

                python:
                    import random
                    esclamazioni = ["EUREKA!", "CI SONO!", "HO CAPITO!", "MACCERTO!"]
                    esclamazione = random.choice(esclamazioni)

                text esclamazione:
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

        null height 30

        # separator if answer present
        if ans_right > 0:
            add separator_eureka:
                xalign 0.0
                xoffset -20
        else:
            add separator_think:
                xalign 0.0
                xoffset -20


        null height 30
        # correct answer
        text right["answers"][ans_right]:
                xalign 0.0
                textalign 0.0
                xsize 600
                outlines [(0, "#000")]
                color "#000"
                size 35
                font "static/Caveat-Regular.ttf"

    # Topic Bookmarks
    vbox:
        xsize 200
        xalign 0.122
        yalign 0.1
        spacing 20

        imagebutton:
            idle black_bm
            hover black_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,0), With(Pixellate(0.6,3))]

        imagebutton:
            idle red_bm
            hover red_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,1), With(Pixellate(0.6,3))]

        imagebutton:
            idle green_bm
            hover green_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,2), With(Pixellate(0.6,3))]

        imagebutton:
            idle blue_bm
            hover blue_bm_ext
            hover_xoffset 5
            action [Function(Taccuino.tq().show_index_page,0,3), With(Pixellate(0.6,3))]



    # PAGE TURN

    $ current_page = (left["title"], right["title"])

    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.95
            idle fw
            hover fw_h


            action [Function(Taccuino.tq().turn_question_page, True, current_page), With(Pixellate(0.6,3))]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.95
            idle bw
            hover bw_h
            action [Function(Taccuino.tq().turn_question_page, False, current_page), With(Pixellate(0.6,3))] # blinds

    imagebutton:
            xalign 0.01
            yalign 0.5
            idle im.Scale("overlay/notes_icon.png", 50, 50)
            hover im.Scale("overlay/notes_icon.png", 100, 100)
            action [Function(hide_notebook), With(easeoutbottom)]