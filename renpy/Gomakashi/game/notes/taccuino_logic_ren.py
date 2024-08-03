"""renpy
init python:
"""
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
        self.current_topic = 0  # MAKE THIS AN ENUM

        self.tq_data = {}
        self.titles = []

        with renpy.open_file("notes/notes.json") as file:
            self.tq_data = json.load(file)

        self.titles = [page_data['title'] for page_data in self.tq_data["0"].values()]

    # Signleton
    @staticmethod
    def tq():
        if Taccuino.instance is None:
            Taccuino.instance = Taccuino()

        return Taccuino.instance

    # calls the index screen
    def show_index_page(self, page=None, topic=None, persistent_bookmark=True):
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
        fw = False if (page + 1) * self.per_page == len(padded_titles) else True

        this_page = padded_titles[page * self.per_page:(page + 1) * self.per_page]

        renpy.hide_screen("tq_question_page")
        renpy.show_screen("tq_index_page", this_page=this_page, forward=fw, backward=bw, pb=persistent_bookmark)




    def turn_index_page(self, forward: bool):
        self.index_page = self.index_page + 1 if forward else self.index_page - 1
        self.show_index_page()

    def show_question_page(self, title):
        print("Showing specific page for:\n" + title)

        paired_titles = pair_titles(self.titles)

        page = ()
        for pair in paired_titles:
            if title in pair: page = pair

        #set_as_seen(page)

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
