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

    #finds and returns the item in "list" that is "distance" steps removed from base, or none if the list runs out


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
                self.tq_data = json.load(file)["-Topic1-"]
                #TODO handle topics

            #titles = ["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit",
            #"tit9", "tit8", "tit7", "tit6", "tit5"]

            self.titles = list(self.tq_data.keys())



        #Signleton
        @staticmethod
        def tq():
            if Taccuino.instance is None:
                Taccuino.instance = Taccuino()

            return Taccuino.instance

        #calls the index screen
        def show_index_page(self, page = None, topic=None):
            if page is None: page = self.index_page
            if topic is None: topic = self.current_topic


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



            first = paired_titles[0]
            last = self.titles[-1]


            bw = False if page == paired_titles[0] else True
            fw = False if page == paired_titles[-1] else True


            left = self.tq_data[page[0]]
            right = self.tq_data[page[1]]

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

    $print(renpy.current_screen())




# tq : Taccuino object
screen tq_index_page(this_page, forward, backward):
    zorder 102
    modal True
    # this_page := list of titles in the current page



    $bw = im.Scale("overlay/bw.png", 70, 40)
    $fw = im.Scale("overlay/fw.png", 70, 40)
    $bw_h = im.Scale("overlay/bw_h.png", 70, 40)
    $fw_h = im.Scale("overlay/fw_h.png", 70, 40)


    vbox:
        xalign 0.5

        null height 130

        grid 2 7:

            xspacing 700
            yspacing 70
            for t in this_page:
                textbutton t:
                    default_focus 10
                    text_style "note_titles"
                    action Function(Taccuino.tq().show_question_page, t)



    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.9
            idle fw
            hover fw_h


            action [Function(Taccuino.tq().turn_index_page, True), With(Pixellate(0.5,1))]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.9
            idle bw
            hover bw_h
            action [Function(Taccuino.tq().turn_index_page, False), With(blinds)]

    imagebutton:
            xalign 0.01
            yalign 0.5
            idle im.Scale("overlay/notes_icon.png", 50, 50)
            hover im.Scale("overlay/notes_icon.png", 100, 100)
            action [Function(hide_notebook), With(easeoutbottom)]


screen tq_question_page(left, right, forward, backward):
    # left := dict - data of the left page
    # right := dict - data of the right page, or None if not present
    # forward := bool - is there a next page?
    # backward := bool - is there a previous page?

    zorder 102
    modal True

    python:
        bw = im.Scale("overlay/bw.png", 70, 40)
        fw = im.Scale("overlay/fw.png", 70, 40)
        bw_h = im.Scale("overlay/bw_h.png", 70, 40)
        fw_h = im.Scale("overlay/fw_h.png", 70, 40)



    vbox:
        xalign 0.33

        null height 130

        text left["title"]


    vbox:
        xalign 0.66

        null height 130

        text right["title"]


    $ current_page = (left["title"], right["title"])

    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.9
            idle fw
            hover fw_h


            action [Function(Taccuino.tq().turn_question_page, True, current_page), With(Pixellate(0.5,1))]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.9
            idle bw
            hover bw_h
            action [Function(Taccuino.tq().turn_question_page, False, current_page), With(blinds)]

    imagebutton:
            xalign 0.01
            yalign 0.5
            idle im.Scale("overlay/notes_icon.png", 50, 50)
            hover im.Scale("overlay/notes_icon.png", 100, 100)
            action [Function(hide_notebook), With(easeoutbottom)]