import json
with open("notes.json") as file:
    dict = json.load(file)["-Topic1-"]
    print([page_data['title'] for page_data in dict.values()])