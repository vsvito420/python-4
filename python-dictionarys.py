schueler = {
    "name": "Max Mustermann",
    "alter": 15,
    "stadt": "Friedrichshafen",
    "schule": "KMG",
    "note": {
        "Mathe": "3",
        "Deutsch": "2"
    }
}

print("Gibt alles von Schueler aus:")
print(schueler["note"])

print(" ")
print("Nachher:")


note = schueler["note"]
deutsch = note["Deutsch"]

# Greife auf Schueler > Note > note von Deutsch
print(schueler["note"]["Deutsch"])
