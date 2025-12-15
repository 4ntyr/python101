def namen_normalisieren(langer_name):
    teile = langer_name.split()
    if len(teile) == 1:
        return teile[0]

    if len(teile) == 1:
        return f"{teile[0]}".strip()

    nachname = teile[-1]
    vornamen = teile[:-1]

    kurz_vornamen = []

    for i, teil in enumerate(vornamen):
        if teil.islower():
            nachname = " ".join(teile[i:])
            vornamen = vornamen[:i]
            break

    for vorname in vornamen:
        if "." in vorname:
            aka = vorname + " "
            kurz_vornamen.append(aka)
            continue
        if "-" in vorname: 
            teile_bindestrich = vorname.split("-")
            gekuerzt = "-".join([t[0] + "." for t in teile_bindestrich if t])
            kurz_vornamen.append(gekuerzt)
            continue
        else:
            kurz_vornamen.append(vorname[0] + ".")

    kurz_vorname = "".join(kurz_vornamen)
    name_kurz = f"{kurz_vorname} {nachname}".strip()

    return " ".join(name_kurz.split())

assert namen_normalisieren("Kula") == "Kula"
assert namen_normalisieren("Anton Kula") == "A. Kula"
assert namen_normalisieren("Anton Frank Kula") == "A.F. Kula"
assert namen_normalisieren("Anton-Frank Kula") == "A.-F. Kula"
assert namen_normalisieren("Anton-Frank-Chris Kula") == "A.-F.-C. Kula"
assert namen_normalisieren("Anton Frank von Kula") == "A.F. von Kula"
assert namen_normalisieren("Anton Frank zu Kula-Quandt") == "A.F. zu Kula-Quandt"
assert namen_normalisieren("Anton Frank von Kula und Quandt") == "A.F. von Kula und Quandt"
assert namen_normalisieren("Dr. Anton Kula") == "Dr. A. Kula"
assert namen_normalisieren("Dipl.-Ing. Anton Kula") == "Dipl.-Ing. A. Kula"
assert namen_normalisieren("Dr. Anton Frank Kula") == "Dr. A.F. Kula"
assert namen_normalisieren("Dr. Anton von Kula") == "Dr. A. von Kula"
assert namen_normalisieren("Dr. Anton Frank von Kula") == "Dr. A.F. von Kula"
assert namen_normalisieren("Prof. Anton Frank von Kula") == "Prof. A.F. von Kula"
print("No assertion error. All names are processed as instructed.")
