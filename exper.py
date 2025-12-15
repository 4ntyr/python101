print("1a")
original = [1,2,3,4,5]
kopie = original
original[2] = 42
print(f"Original: {id(original)}")
print(f"Kopie: {id(kopie)}")
print(f"Output: {kopie}")

print("1b")
original = "tisch"
kopie = original
original = "stuhl"
print(f"Original: {id(original)}")
print(f"Kopie: {id(kopie)}")
print(f"Output: {kopie}")


print("2")
def hmm(liste):
    liste[0] = "Anfang der Liste"
    liste.append("Ende der Liste")
    return "Fertig :-)"
a = [1,2,3,4,5]
print("Die append-Funktion fügt die Eingabe als neuen Eintrag hinzu,\ndas setzen eines Listenplatzes überschreibt den Eintrag")
hmm(a)
print(a)


print("3")
def korrigiere(wb):
    wb["freund"] = "eve"
    wb["feind"] = "alice"
daten = {"alter": 42, "name": "alice", "freund": "bob", "feind": "eve"}
print(f"Freund vorher: {id(daten['freund'])}")
print(f"Feind vorher: {id(daten['feind'])}")
korrigiere(daten)
print(f"Freund danach: {id(daten['freund'])}")
print(f"Feind danach: {id(daten['feind'])}")
print(daten)


print("4a")
shared = [0]
liste = [shared] * 5
liste[2][0] = 42
print(f"Shared: {id(shared)}")
print(f"Liste: {id(liste)}")
for eintrag in liste:
    print(f"Listeneintrag: {id(eintrag)}")
print(liste)
print(shared)


print("4b")
shared = 0
liste = [shared] * 5
liste[2] = 42
print(f"Shared: {id(shared)}")
print(f"Liste: {id(liste)}")
for eintrag in liste:
    print(f"Listeneintrag: {id(eintrag)}")
print(liste)
print(shared)

print("5")
def change(wert):
    wert += 1
a = 5
print(id(a))
change(a)
print(id(a))
print(a)