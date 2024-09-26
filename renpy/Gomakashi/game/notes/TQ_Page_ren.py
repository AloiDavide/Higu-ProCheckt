"""renpy
init python:
"""
import json
import math

shrink_factor = 13
shrink_limit = 550

class TQ_Page:

    def __init__(self, page_data):
        self.title = page_data.get("title", "")
        self.question = page_data.get("question", "")
        self.answers = page_data.get("answers", [])
        self.seen = page_data.get("seen", False)
        self.display_answer = page_data.get("display_answer", 0)
        self.reaction = page_data.get("reaction", "CI SONO!")


    def asDict(self):
        return vars(self)

    def get_tsize(self):
        # we can fit about 550 characters at max size between all sections
        text_length = len(self.question) + len(self.answers[self.display_answer])
        shrink = max(0, math.ceil((text_length - shrink_limit) / shrink_factor))

        return 35 - shrink

    def __repr__(self):
        return (f"Page(title={self.title}, \n"
                f"question={self.question}, \n"
                f"answers={self.answers}, \n"
                f"seen={self.seen}, \n"
                f"display_answer={self.display_answer}, \n"
                f"reaction={self.reaction})")



json_string = '''
{
    "title": "Example Title",
    "question": "Example Question?",
    "answers": [
        "Answer 1",
        "Answer 2"
    ],
    "seen": true,
    "display_answer": 1,
    "reaction": "Example Reaction"
}
'''

# json_data = json.loads(json_string)
# page = TQ_Page(json_data)
#
# print(page.asDict())
# print(page)

