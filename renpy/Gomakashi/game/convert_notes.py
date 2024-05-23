import json

def get_ans_index(lst):
    for i, item in enumerate(lst):
        if item.startswith('!'):
            lst[i] = item[1:]
            return i-1
    return 0

#read and store title
#Keep reading until you find

titles = ["notes0.txt", "notes1.txt", "notes2.txt"]
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
                    'display_answer': answer_index
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



