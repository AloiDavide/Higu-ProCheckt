"""renpy
init python:
"""
import json


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

json_data = json.loads(json_string)
page = TQ_Page(json_data)

print(page.asDict())