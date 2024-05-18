import json


#read and store title
#Keep reading until you find

with open("notes.txt", encoding="utf-8") as txt:
    content = txt.read()

result = {}

pages = content.split("---")


for page in pages:
    if page.strip():  # ignore any empty pages
        sections = page.strip().split('-')

        title = sections[0].strip()
        question = sections[1].strip()
        answers = [section.strip() for section in sections[2:] if section.strip()]
        answers.insert(0, "")

        result[title] = {
                'title': title,
                'question': question,
                'answers': answers,
                'seen' : False,
                'display_answer': 0
        }

result = {"-Topic1-": result}

print(json.dumps(result, indent=4))
json.dump(result, open("notes.json", "w", encoding="utf-8"), indent=4)



