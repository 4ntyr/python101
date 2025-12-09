import json

with open("dict.json", "r") as fp:
    dict = json.load(fp)

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
    while True:
        mode = str(input("Was willst du tun?: ")).lower() # Add, Translate, Edit, X=Cancel

        if mode == "t":
            input_buffer = input("Welches Wort?: ")
            print(f"Die Übersetzung für {input_buffer} ist {search(input_buffer)}.")
        elif mode == "a":
            change(input("Welches DEUTSCHE Wort willst du hinzufügen?: "))
        elif mode == "e":
            edit(input("Die Übersetzung von welchem DEUTSCHEN Wort willst du ändern?: "))
        elif mode == "x":
            break
        else:
            print("Somethings wrong.")
        
        with open("dict.json","w") as fp:
            json.dump(dict, fp, indent=2)

main()
