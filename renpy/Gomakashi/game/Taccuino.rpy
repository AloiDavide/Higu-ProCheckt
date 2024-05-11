init python:
    import json


    def show_notebook():
        renpy.show_screen("taccuino")
        Taccuino.getTQ().show_index_page()

    #for now it returns a list with the titles, eventually with the jsons
    def get_pages():
        titles = [["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit"], ["tit", "tit", "tit", "tit", "tit", "tit"]]
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

            fw = False if page == 0 else False
            bw = False if page == len(self.pages)-1 else False

            renpy.show_screen("tq_index_page", this_page=self.pages[page], forward=fw, backward=bw)

        def turn_index_page(self, forward: bool):
            self.current_page = self.current_page+1 if forward else self.current_page-1
            self.show_index_page()


        def show_topic(self, topic):
            pass



#-----------------------------------------------------------------

screen taccuino():
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)
    add taccuino_overlay

# tq : Taccuino object
screen tq_index_page(this_page, forward, backward):

    grid 2 4:
        for t in this_page:
            text t