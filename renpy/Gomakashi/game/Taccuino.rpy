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
    $taccuino_overlay = im.Scale("overlay/taccuino.png", 1920, 1080)


    add taccuino_overlay
    #play multiple pages flipping sound

    textbutton 'Taccuino':
        style "menu_buttons"
        text_style "menu_text"
        action ToggleScreen("taccuino", transition=easeoutbottom)
