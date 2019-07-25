import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def function(word):
    if word in data:
        return data[word]                                                                                                               # if word is a key then return value
    
    elif len(get_close_matches(word,data.keys())) > 0:                                                                                  # if close matches are > 0 
        choice = input("Did you mean %s instead ? Press Y if Yes, N if No" % get_close_matches(word,data.keys())[0])                    # get_close_matches returns a list of close matches
        if choice =="Y":
            return data[get_close_matches(word,data.keys())[0]]                                                                         # retrun value of new suggested key
        elif choice =="N":
            return "The word doesnt exist. Please double check."
        else:
            return "We didnt understand your entry !"
    
    else:
        return "The world doesnt exist. Please double check."

while 1:
    word = input("Enter the word :")
    new_word = word.lower()

    print(function(new_word))
