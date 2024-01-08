init python:

    class Question(object):


        def __init__(self, text, requirements=[]):
            self.text = text
            self.seen = False
            self.requirements = requirements
            self.show = not requirements

        def canShow(self):
            if self.seen: return False

            if not self.requirements: return True

            return all(ques[q].seen for q in self.requirements)

        def tickOff(self):
            self.seen = True


    ques = {"where":Question('Dove siamo?',[]),
            "whoBern":Question('Chi o cosa sei tu?',[]),
            "poems":Question('Il tuo nome non mi è nuovo.',[]),
            "after":Question('Cosa è successo a Larry dopo la mia morte?',[]),
            "whoMe":Question('Cosa sono io?',["whoBern", "where"]),
            "tea":Question('Vorrei un\'altra tazza di tè.',["whoMe"]),
            "rules":Question('Regole?! Quali regole?',["after"]),
            "whyMe":Question('Quindi è per questo che mi hai scelto.',["whoMe","rules"]),
            "end":Question('Tiriamo le somme.',["whyMe", "rules", "poems", "tea"])#
    }