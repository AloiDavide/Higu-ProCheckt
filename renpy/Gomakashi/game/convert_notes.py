import json
import random
esclamazioni = ["EUREKA!", "CI SONO!", "HO CAPITO!", "MACCERTO!"]
def get_ans_index(lst):
    for i, item in enumerate(lst):
        if item.startswith('!'):
            lst[i] = item[1:]
            return i-1
    return 0


#This reads a series of notes files and stores all the data in a single json
def parse_notes():
    titles = ["misteri_principali.txt", "serie_omicidi.txt", "misteri_wata.txt", "misteri_esterni.txt"]
    contents = []
    for title in titles:

        with open(title, encoding="utf-8") as txt:
            contents.append(txt.read())


    result = {}
    id = 0
    for content in contents:

        topic_dict = {}
        pages = content.split("---")

        for page in pages:
            seen = True
            if page.startswith('!'):
                seen = False
                page = page[1:]

            if page.strip():  # ignore any empty pages
                sections = page.strip().split('\n-')

                answer_index = get_ans_index(sections)

                title = sections[0].strip()
                question = sections[1].strip()
                answers = [section.strip() for section in sections[2:] if section.strip()]
                answers.insert(0, "")

                topic_dict[title] = {
                        'title': title,
                        'question': question,
                        'answers': answers,
                        'seen' : seen,
                        'display_answer': answer_index,
                        'reaction': random.choice(esclamazioni)
                }

        topic_dict.update({"": {
                    "title": "",
                    "question": "",
                    "answers": [
                        ""
                    ],
                    "seen": True,
                    "display_answer": 0
                }
        })

        result[id] = topic_dict

        id += 1

    print(json.dumps(result, indent=4))
    json.dump(result, open("notes.json", "w", encoding="utf-8"), indent=4)


def uncheck_all(file):
    with open(file, "r", encoding="utf-8") as notes:
        lines = notes.readlines()

    with open(file, "w", encoding="utf-8") as notes:
        for line in lines:
            if line.strip() == "---":
                line = line.replace("---", "---!")
            notes.write(line)

def randomize_exclamations():
    pass
    #TODO

parse_notes()

#uncheck_all("misteri_wata.txt")

#Implement the reverse function in case we need to make big time changes again