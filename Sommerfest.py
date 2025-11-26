def namen_normalisieren(name):
    teile = name.split()
    if len(teile) == 1:
        return teile[0]

    akademischer_titel = ""
    if teile[0] == "Dr.":
        akademischer_titel = "Dr."
        teile = teile[1:]

    if len(teile) == 1:
        return f"{akademischer_titel} {teile[0]}".strip()

    nachname = teile[-1]
    vornamen = teile[:-1]

    kurz_vornamen = []

    ADEL = {"von", "zu", "der", "und"}

    for i, teil in enumerate(vornamen):
        if teil.lower() in ADEL:
            nachname = " ".join(teile[i:])
            vornamen = vornamen[:i]
            break

    for vorname in vornamen:
        if "-" in vorname: 
            teile_bindestrich = vorname.split("-")
            gekuerzt = "-".join([t[0] + "." for t in teile_bindestrich if t])
            kurz_vornamen.append(gekuerzt)
        else:
            kurz_vornamen.append(vorname[0] + ".")

    kurz_vorname = "".join(kurz_vornamen)
    name_kurz = f"{akademischer_titel} {kurz_vorname} {nachname}".strip()

    return " ".join(name_kurz.split())

assert namen_normalisieren("Kula") == "Kula"
assert namen_normalisieren("Anton Kula") == "A. Kula"
assert namen_normalisieren("Anton Frank Kula") == "A.F. Kula"
assert namen_normalisieren("Anton-Frank Kula") == "A.-F. Kula"
assert namen_normalisieren("Anton Frank von Kula") == "A.F. von Kula"
assert namen_normalisieren("Anton Frank zu Kula-Quandt") == "A.F. zu Kula-Quandt"
assert namen_normalisieren("Anton Frank von Kula und Quandt") == "A.F. von Kula und Quandt"
assert namen_normalisieren("Dr. Anton Kula") == "Dr. A. Kula"
assert namen_normalisieren("Dr. Anton Frank Kula") == "Dr. A.F. Kula"
assert namen_normalisieren("Dr. Anton von Kula") == "Dr. A. von Kula"
assert namen_normalisieren("Dr. Anton Frank von Kula") == "Dr. A.F. von Kula"
print("No assertion error")
