init python:
    class Question(object):
        def __init__(self, text, unlocks=[], unlocked=False):
            self.text = text
            self.unlocked = unlocked
            self.unlocks = unlocks

        def unlock(self):
            self.unlocked=True

        def lock(self):
            self.unlocked=False
