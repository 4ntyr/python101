
eingabe = list(input("Prüfe: "))
def reduziere(list1):
    res_list = []
    i=0
    while i<len(list1):
        if list1[i] == "(" or list1[i] == ")":
            res_list.append(list1[i])
        i+=1
    return(res_list)
def klammer_check(list1):
    i = a = z = x = 0
    while i < len(list1):
        if list1[i] == "(":
            a += 1
        elif list1[i] == ")":
            z += 1
        if a < z:
            break
        i += 1
    if a != z:
       x = 1
    if x == 0 :
        return("Klammern korrekt")
    else:
        return("Klammern fehlerhaft.")


print(reduziere(eingabe))
print(klammer_check(eingabe))