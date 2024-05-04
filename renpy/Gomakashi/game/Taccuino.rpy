python:
    class Taccuino:
        def __init__(self):
            self.topics = []

        def add_topic(self, topic):
            self.topics.append(topic)

    class Topic:
        def __init__(self, name):
            self.name = name
            self.pages = []

    class Page:
        def __init__(self, title, question, answer, seen):
            self.title = title
            self.question = question
            self.answer = answer
            self.seen = seen


screen taccuino():


    python:
        taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)

        #max 8 per page
        titles = ["tit1", "tit2", "tit3", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit", "tit"]

    add taccuino_overlay
    #play multiple pages flipping sound


    vbox:

        yalign 0
        xalign 0.3
        spacing 50
        null height 50
        for t in titles:
            textbutton t:
                default_focus 10
                text_style "note_titles"
                action ToggleScreen("taccuino", transition=easeoutbottom)
