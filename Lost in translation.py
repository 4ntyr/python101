import json

with open("dict.json", "r") as fd:
    dict = json.load(fd)

def search(input):
    if input in dict.keys():
        res = dict[input]
        return res
    elif input in dict.values():
        for key,value in dict.items():
            if value == input:
                res = key
                return res
    else:
        return "nicht gespeichert"

def change(german_word):
    english_word = input("Was ist die Übersetzung?: ")
    dict[german_word] = english_word

def edit(german_word):
    english_word = input("Was ist die englische Übersetung?: ")
    if german_word not in dict:
        print("Dictionary returned an error: Word does not exist yet.")
    else:
        dict[german_word] = english_word

def main():
    mode = str(input("Was willst du tun?: ")) # Add, Tranlate, Edit

    if mode == "T":
        input_buffer = input("Welches Wort?: ")
        print(f"Die Übersetzung für {input_buffer} ist {search(input_buffer)}.")
    elif mode == "A":
        change(input("Welches DEUTSCHE Wort willst du hinzufügen?: "))
    elif mode == "E":
        edit(input("Die Übersetzung von welchem DEUTSCHEN Wort willst du ändern?: "))
    else:
        print("Somethings wrong.")
    
    with open("dict.json","w") as fd:
        json.dump(dict, fd, indent=2)
while True:
    main()

