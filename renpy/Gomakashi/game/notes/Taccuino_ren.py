"""renpy
init python:
"""

import json
from enum import Enum
from game.notes.TQ_Page_ren import TQ_Page


PER_PAGE = 14
class Topic(Enum):
    MAIN = 0
    PAST = 1
    ONI = 2
    WATA = 3
    TATARI = 4
    EXTERNAL = 5





class TQ:
    _instance = None

    def __init__(self):
        print("TQ init...")
        self.showing = False
        self.per_page = 14
        self.index_page = 0
        self.current_topic = 0

        self.tq_raw = {}
        self.tq_dictionary = {}
        self.titles = []

        with renpy.open_file("notes/notes.json") as file:
            self.tq_raw = json.load(file)
            print(self.tq_raw)

        for topic in self.tq_raw:
            print(topic)
            self.tq_dictionary[topic] = []

            for page in self.tq_raw[topic].values():
                page_obj = TQ_Page(page)
                self.tq_dictionary[str(topic)].append(page_obj)

        # I did it, I have four lists of page objects grouped by topic
        # self.titles = [page_data['title'] for page_data in self.tq_data["0"].values()]

    @staticmethod
    def get():
        if TQ._instance is None:
            TQ._instance = TQ()

        return TQ._instance

    @staticmethod
    def reload():
        TQ._instance = TQ()

        return TQ._instance

    def show(self):
        if self.showing:
            return

        renpy.show_screen("taccuino")
        self.show_index_page()
        self.showing = True


    def hide(self):
        renpy.hide_screen("taccuino")
        renpy.hide_screen("tq_index_page")
        renpy.hide_screen("tq_question_page")
        self.showing = False

    def show_index_page(self, index_page=None, topic=None, persistent_bookmark=True):
        if index_page is None:
            index_page = self.index_page
        else:
            self.index_page = index_page
        if topic is None:
            topic = self.current_topic
        else:
            self.current_topic = topic


        pages = self.tq_dictionary[str(topic)]
        titles = [page.title for page in pages]

        bw = False if index_page == 0 else True
        fw = False if index_page == int( len(titles)-1 / self.per_page ) else True

        if fw:
            visible = titles[index_page * self.per_page : (index_page + 1) * self.per_page]
        else:
            visible = titles[index_page * self.per_page :]

        renpy.hide_screen("tq_question_page")
        renpy.show_screen("tq_index_page", titles=visible, forward=fw, backward=bw, pb=persistent_bookmark)

    def turn_index_page(self, forward: bool):
        self.index_page = self.index_page + 1 if forward else self.index_page - 1
        self.show_index_page()



#return json.dumps(vars(self), indent=4)