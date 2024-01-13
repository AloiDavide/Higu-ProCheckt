init -1 python:
    import random
    def rand():
        return random.uniform(0, 2)

init -1 python:
    import functools

    def lipflap(event, name="", mouths=[], interact=True, **kwargs):
    #sub check with generic character using functools and passing name
        if renpy.get_attributes(name)==None: return

        attr = mouths[0]
        for a in renpy.get_attributes(name):
                a=a.split("_")[0]
                if a in mouths:
                    attr = a


        if event == "show":
            renpy.show(name+" "+attr+"_talk")

        elif event == "slow_done":
            renpy.show(name+" "+attr)
            renpy.restart_interaction()

init -1 python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

init -1 python:

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