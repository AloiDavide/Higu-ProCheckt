init python:
    import json
    import


    def test():
        renpy.return_statement()
    #for now it returns a list with the titles, eventually with the jsons
    def get_notes():
        titles = ["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit"]
        return titles

    #splits the list into a list of lists, each with the elements of one page
    #returns the new list and the shape of the last element
    def split_pages(input, Nrows):
        n = Nrows*2
        pages = [input[i:i+n] for i in range(0, len(input), n)]
        return pages

    class Taccuino:
        current_page = 0
        current_topic = 0 #MAKE THIS AN ENUM

        def __init__(self, pages):
            self.pages = pages

        #signleton
        @staticmethod
        def getTQ():
            pass

        #calls the index screen
        def show_index_page(page = current_page, topic=current_topic):
            fw = False if page == 0 else False
            bw = False if page == len(self.pages)-1 else False

            renpy.show_screen("tq_index_page", tq=self, this_page=self.pages[page_n], forward=fw, backward=bw)

        def turn_index_page(forward: bool):
            current_page = current_page+1 if forward else current_page-1



        def show_topic(topic):
            pass



    import json



    #max 8 per page
    titles = ["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit"]
    pages = split_pages(titles, 8)
    leftover = len(pages[-1])

    print(pages)
    print(leftover)

screen taccuino():
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)
    $tq = Taccuino.getTQ()

    add taccuino_overlay

    tq.show_index_page()

# tq : Taccuino object
screen tq_index_page(tq, this_page, turns_left, turns_right):


    grid 2 4:
        text "a"
        text "a"
        text "b"
        text "b"
        text "c"
        text "c"
        text "d"
        text "d"