def namen_normalisieren(name):
    teile = name.split(" ")
    vornamen = teile[:-1]
    nachname = teile[-1]
    name_kurz = ""
    adel = {"von", "zu", "der", "und"}
    for vorname in vornamen:
        if vorname.endswith("."): # Dr titel und so
            name_kurz += vorname + " "
        elif "-" in vorname: # doppelnamen 
            teile_vorname = vorname.split("-")
            for teil in teile_vorname:
                name_kurz += teil[0] + ".-"
            name_kurz = name_kurz[:-1] + " "
        elif vorname.lower() in adel: # adelstitel
            name_kurz += vorname + " "
        else:
            name_kurz += vorname[0] + ". " # normie name (langweilig 😪😴)
    name_kurz += nachname

    return name_kurz

testname1 = "Gesine Dachs"
testname2 = "Fabian-Wilhelm Jonathan Müller"
testname3 = "Karl-Heinz von Brühl"
testname4 = "Adelbert von Kula-Quadt"
testname5 = "Dr. med. Franz Wilhelm-Karl von und zu Schmidt"
kurz = namen_normalisieren(testname5)
print(kurz)