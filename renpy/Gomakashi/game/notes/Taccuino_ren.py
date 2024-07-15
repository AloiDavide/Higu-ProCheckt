"""renpy
init python:
"""
import json
from enum import Enum

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

        self.index_page = 0
        self.current_topic = 0

        self.tq_data = {}
        self.titles = []

        with renpy.open_file("notes/notes.json") as file:
            tq_data = json.load(file)

        for topic in tq_data:
            to

        self.titles = [page_data['title'] for page_data in self.tq_data["0"].values()]

    @staticmethod
    def get():
        if TQ._instance is None:
            TQ._instance = TQ()

        return TQ._instance

    def show_index_page(self, page=None, topic=None):
        pass


    def turn_index_page(self, forward: bool):
        self.index_page = self.index_page + 1 if forward else self.index_page - 1
        self.show_index_page()



#return json.dumps(vars(self), indent=4)