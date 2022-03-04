from difflib import get_close_matches
import json

f = open("data.json")

data = json.load(f)
while data:
    print("------------------------------------------------------------------")
    print("Search the meaning of the word:")
    text = input().lower()
    close_match = get_close_matches(text,data.keys())[0]
    if text in data:
        meaning = data[text]
        print("--------------------------------Meaning----------------------------\n")
        for i in meaning:
            print(i,"\n")
    elif close_match:
        print("Do you mean %s?\n If Yes press Y or press N"% close_match)
        user_consent = input().lower()
        if user_consent == 'y':
            meaning = data[close_match]
            print("--------------------------------Meaning----------------------------\n")
            for i in meaning:
                print(i,"\n")
        else:
            print("Word Does not exist...")
    else:
        print("Word Does not exist...")