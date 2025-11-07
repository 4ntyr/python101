aufzeichnungen = [
    2, 3, -4, 5, 6, 5, 4, -6, 2, -1, -4, -2, -5, -4, -3, -1, -2, 1, -2, -4, -4,
    -3, -4, -3, 7, -2, -4, 3, 1, -2, 2, -8, 10, 1, -3, 3, -3, -1, -2, -5, 2, -2,
    -1, -2, -5, -9, 2, 5, 6, -4, -1, -2, -5, -3, -2, 6, -3, -1, -6, 5, -6, 1,
    -3, -3, -1, -3, 5, 5, 4, -5, -8, 6, 4, 5, -12, -6, 2, 4, -9, 10, -7, -4, 2,
    1, -1, -3, -2, 4, -3, 1, -1, 2, -3, -7, -3, -8, -1, 12, -2, -4, -13, -2, -8,
    -2, 12, -4, 7, -2, -8, 5, 1, 4, 1, -5, 7, -3, 4, -3, -4, 2, 4, -4, -1, 3,
    -9, 3, -1, 1, 2, 6, 2, -4, -5, -2, 9, 2, 6, -4, -2, -2, 6, 2, 7, 3, -1, 6,
    -2, 9, 3, 4, -5, 10, 1, -12, -7, -2, 2, -5, 1, 10, -1, -5, 2, 7, 11, -2, 9,
    -5, -3, -6, -6, -1, -4, -3, 3, 1, 9, -6, -7, 5, 5, 1, 9, 5, -2, 1, -2, -4,
    9, 1, -3, 8, 3, -6, -3, 3, -1, -10, 3, -2, 5, 4, -1, 3, 1, 2, -2, 9, 7, -1,
    -7, -2, 10, -6, -2, 12, -3, -2, -2, -7, -1, 3, 3, -4, 8, -1, 8, -2, -12, 6,
    -4, -2, -4, 3, 3, 2, -9, -2, 1, 4, -4, -2, -3, -1, -6, 1, 5, 2, 5, -2, 3,
    -1, 4, -6, 4, 8, -1, 7, -3, 1, -3, -2, 5, -2, -4, 3, 8, 1, 1, -9, 4, -1, 8,
    8, -6, 3, 2, 12, 8, 6, 6, 4, -7, 3, 8, 3, -3, -7, 7, -3, -4, 7, -8, 3, 5, 3,
    -4, -2, 1, -6, -8, -3, -6, 6, 1, 7, -8, -2, 4, 1, 7, -4, 3, 2, 7, -3, -7,
    -9, 5, 8, 2, 5, -2, -6, 2, 3, -4, 1, 1, 5, -5, 3, 2, -11, 4, 1, -3, 3, -7,
    -5, -7, 3, -1, -1, 3, 5, -2, 5, 4, -5, 5, 2, 5, 4, 2, 5, -4, -5, -1, 6, 8,
    -2, -5, -2, 7, -4, 8, -12, 6, -7, 1, -1, -3, 4, -1, 3, 1, 3, 5, 4, 4, 4, -2,
    6, -3, -10, 1, -9, 4, -10, 4, -3, 8, -3, 5, -4, -4, -4, -4, 5, -1, -3, -2,
    -2, 9, -1, -1, -4, -3, 10, 4, -3, -6, -2, -2, 3, 5, -6, 3, -1, 6, -1, -4,
    -9, -2, 4, 1, 5, -6, 2, 1, -3, 4, 6, -1, -2, 7, -3, -11, 2, -4, 3, -3, 4, 4,
    -1, -1, -3, 2, 6, -3, -1, -1, -1, -5, 5, 3, -3, 3, 3, -5, 1, -6, -13, 5, -2,
    4, -2, 1, -2, 6, 3, 2, -10, -3, -2, 10, 4, -11, 6, -5, -4, 2, -2, -2, 9, 1,
    2, 5, -1, 4, -8, 1, -5, 3, 1, 1, -10, -1, -2, -1, 1, 5, 4, -2, -1, 6, 2, -2,
    6, 1, 1, 4, -4, 2, -7, 4, -5, 3, -5, 4, -5, 2, -1, 1, -10, 3, -8, 8, 2, 8,
    -3, 6, 2, -3, -5, 10, -2, 2, 11, -3, 4, -2, 6, -7, 3, 10, 5, 13, 10, -2, -3,
    1, 9, -5, 6, -1, -10, -8, -5, -6, -1, -4, 5, 9, -1, 3, -8, 4, -6, 3, -6, -8,
    1, 4, 9, 2, -8, 10, -2, 11, -7, -9, -10, 4, -1, -7, -1, 3, -7, 2, -7, -5, 5,
    3, 2, 1, -1, 6, 6, -2, -5, -1, -5, -4, 1, 1, -1, 6, -2, -5, -2, 7, 8, -4,
    -1, -1, 1, -4, 2, -3, -3, 2, 2, 1, -2, -2,   
]
besuchte_etagen = []
betrag_liste = []
einweg_zusammengefasst = [0,]
post_switch_aufenthalte = [0,]
aktuelle_etage = 0
fünfzig_check = 0

def länge(list):
    a = 0
    for _ in list:
        a += 1
    return a

def high(list):
    a = 0
    for i in list:
        if i > a:
            a = i
    return(a)

def low(list):
    a = 0
    for i in list:
        if i < a:
            a = i
    return(a)

def betrag(zahl):
    if zahl < 0:
        zahl = zahl * -1
    return(zahl)

def summe(list):
    a = 0
    for i in list:
        a += i
    return a

def vorkommen(x ,list):
    a = 0
    for i in list:
        if i == x:
            a += 1
    return(a)

def häufigst(list):
    high = 0
    count = 0
    for i in list:
        if vorkommen(i, list) > count:
            high = i
            count = vorkommen(i, list)
    return(high)     

def erweitere(value, list):
    list += [value]
    return list

for i in range(0, länge(aufzeichnungen)):
    aktuelle_etage = aktuelle_etage + aufzeichnungen[i]
    erweitere(aktuelle_etage, besuchte_etagen)

for i in range(0, länge(aufzeichnungen)):
    a = betrag(aufzeichnungen[i])
    erweitere(a, betrag_liste)

for i in range(länge(aufzeichnungen)):
    fünfzig_check += aufzeichnungen[i]
    if fünfzig_check == 50:
        hate = i
        break

schnitt = summe(betrag_liste) / länge(aufzeichnungen)
strecke = (3*summe(betrag_liste))/1000

j = 0
for i in range(0, länge(aufzeichnungen)):
    if aufzeichnungen[i] > 0 and einweg_zusammengefasst[j] > 0:
        einweg_zusammengefasst[j] += aufzeichnungen[i]
    elif aufzeichnungen[i] > 0 and einweg_zusammengefasst[j] < 0:
        erweitere(0, einweg_zusammengefasst)
        j += 1
        einweg_zusammengefasst[j] += aufzeichnungen[i]
    elif aufzeichnungen[i] < 0 and einweg_zusammengefasst[j] < 0:
        einweg_zusammengefasst[j] += aufzeichnungen[i]
    elif aufzeichnungen[i] < 0 and einweg_zusammengefasst[j] > 0:
        erweitere(0, einweg_zusammengefasst)
        j += 1
        einweg_zusammengefasst[j] += aufzeichnungen[i]
    elif einweg_zusammengefasst[j] == 0:
        einweg_zusammengefasst[j] += aufzeichnungen[i]

j = 0
for i in range(0, länge(besuchte_etagen)):
    if besuchte_etagen[i] > 0 and post_switch_aufenthalte[j] > 0:
        post_switch_aufenthalte[j] += besuchte_etagen[i]
    elif besuchte_etagen[i] > 0 and post_switch_aufenthalte[j] < 0:
        erweitere(0, post_switch_aufenthalte)
        j += 1
        post_switch_aufenthalte[j] += besuchte_etagen[i]
    elif besuchte_etagen[i] < 0 and post_switch_aufenthalte[j] < 0:
        post_switch_aufenthalte[j] += besuchte_etagen[i]
    elif besuchte_etagen[i] < 0 and post_switch_aufenthalte[j] > 0:
        erweitere(0, post_switch_aufenthalte)
        j += 1
        post_switch_aufenthalte[j] += besuchte_etagen[i]
    elif post_switch_aufenthalte[j] == 0:
        post_switch_aufenthalte[j] += besuchte_etagen[i]

fünfzig_check = True
for i in range(0, länge(besuchte_etagen)):
    if vorkommen(i, besuchte_etagen) == 0:
        fünfzig_check = False
        break


# print("Sie haben heute", länge(aufzeichnungen), "Fahrten dokumentiert.") # Aufgabe 1
# print("Sie befinden sich in Etage", etage) # Aufgabe 2
# print("Der Aufzug ist", vorkommen(-1, aufzeichnungen), "mal eine Etage nach unten gefahren") # Aufgabe 3
# #+1 wegen dem Erdgeschoss :-)
print("Das Gebäude hat Etagen von", low(besuchte_etagen), "bis", high(besuchte_etagen), ". Insgesamt also", betrag(low(besuchte_etagen))+betrag(high(besuchte_etagen))+1) # Aufgabe 4
# print("Maximal am Stück wurden", high(betrag_liste), "Etagen zurückgelegt.") # Aufgabe 5
# print("Im Schnitt wurden pro Fahrt", schnitt, "Etagen zurückgelegt.") # Aufgabe 6
# print("Sie haben insgesamt ca.", strecke, "Km zurückgelegt.") # Aufgabe 7
# print("Sie haben", vorkommen(0, etagen_liste), "mal im Erdgeschoss gehalten.") # Aufgabe 8
# print("Sie waren nach der", hate, "Fahrt das erste Mal in der 50 Etage") # Aufgabe 9
# print("Die längste Fahrt am Stück erstreckte sich über", high(einweg_zusammengefasst), "Etagen.") # Aufgabe 10
# print("Am häufigsten waren sie in Etage", most_common(etagen_liste)) # Aufgabe 11
# #-1 weil es um die zahl an wechseln geht und nicht die zahl der aufenthalte
# print("Zwischen Ober- und Untergeschossen wurde", länge(switches)-1,"mal gewechselt.") # Aufgabe 12
# print("Es sind",(not check)*"nicht","alle Etagen im Gebäude abgefahren worden.") # Aufgabe 13