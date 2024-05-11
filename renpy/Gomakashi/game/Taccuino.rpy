init python:
    import json


    def show_notebook():
        renpy.show_screen("taccuino")
        Taccuino.getTQ().show_index_page()

    #for now it returns a list with the titles, eventually with the jsons
    def get_pages():
        tq_data = {}
        with open("static/Caveat-Bold.ttf") as file:
            tq_data = json.load(file)

        titles = tq_data["-topic1-"].keys()
        #titles = [["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit"],
        #["tit9", "tit8", "tit7", "tit6", "tit5"]]

        while len(titles) % 14 != 0:
            titles[-1].append("")
        return titles

    #splits the list into a list of lists, each with the elements of one page
    #returns the new list and the shape of the last element
    def split_pages(input, Nrows):
        n = Nrows*2
        pages = [input[i:i+n] for i in range(0, len(input), n)]
        return pages

    class Taccuino:
        instance = None

        def __init__(self, pages):
            self.current_page = 0
            self.current_topic = 0 #MAKE THIS AN ENUM
            self.pages = pages

        #Signleton
        @staticmethod
        def getTQ():
            if Taccuino.instance is None:
                Taccuino.instance = Taccuino(pages=get_pages())

            return Taccuino.instance

        #calls the index screen
        def show_index_page(self, page = None, topic=None):
            if page is None: page = self.current_page
            if topic is None: topic = self.current_topic

            bw = False if page == 0 else True
            fw = False if page == len(self.pages)-1 else True


            renpy.show_screen("tq_index_page", this_page=self.pages[page], forward=fw, backward=bw)


        def turn_index_page(self, forward: bool):
            self.current_page = self.current_page+1 if forward else self.current_page-1
            self.show_index_page()


        def show_topic(self, topic):
            pass



#-----------------------------------------------------------------

screen taccuino():
    zorder 98
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)
    add taccuino_overlay

# tq : Taccuino object
screen tq_index_page(this_page, forward, backward):
    zorder 99

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
                text t:
                    size 35
                    outlines [(2, "#000")]


    if forward:
        imagebutton:
            xalign 0.85
            yalign 0.9
            idle fw
            hover fw_h


            action [Function(Taccuino.getTQ().turn_index_page, True), With(Pixellate(0.5,1))]

    if backward:
        imagebutton:
            xalign 0.15
            yalign 0.9
            idle bw
            hover bw_h
            action [Function(Taccuino.getTQ().turn_index_page, False), With(blinds)]