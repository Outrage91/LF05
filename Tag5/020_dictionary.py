# Dictionary
# ... ist eine Sammlung von Daten in Python

hund = {
    "name": "Bello",
    "art": "Hund",
    "alter": 5,
    "vermittelt": True
}

# Ein Wörterbuch besteht immer aus "schluessel : wert"

# 1) Werte auslesen
# ... man greift auf den Schlüssel zu um sich den Wert ausgeben zu lassen

# Ausgabe des Namens
print(hund["name"])          # Bello

# Ausgabe des Vermittlungsstandes:
print(hund["vermittelt"])    # True

# 2) Werte ändern

# Der Name des Dictonary[Schlüssel wo der Wert geändert werden soll] = neuer Wert -> der den alten Wert ersetzen soll
hund["alter"] = 6

# Ausgabe des kompletten Dictionaries
print(hund)

# 3) Neue Werte hinzufügen

# Name des Dictionary[Name des neuen Schlüssels] = Wert den wir dem neuen Schlüssel geben (wenn noch nicht vorhanden, wird er neu angelegt!)
hund["lieblingsessen"] = "Käse"

# Ausgabe des kompletten Dictionaries
print(hund)

for schluessel, wert in hund.items():
    print(schluessel, ":", wert)
    
# schluessel, wert -> zwei Variablen mit denen wir arbeiten
# schluessel steht für unseren Schlüssel
# wert steht für den Wert
# in -> gehe durch alle Elemente von ...
# hund.items() -> hund = steht für das Dictionary | .items() -> sagt gib uns bitte den schluessel UND den wert als Paar aus!!!

for schluessel, wert in list(hund.items())[:2]:   # list() -> wandelt die Ausgabe von hund.items() in eine Liste um | [0:2] -> sagt, gib mir nur die ersten 2 Elemente der Liste aus
    print(schluessel, ":", wert)

# 1) items() holt sich alle Einträge
# list() wird das Dictionary in eine Liste umgewandelt
# [:2] begrenzen auf 2 Elemente die uns ausgegeben werden sollen

# 4) Werte löschen
# ... Einträge können einfach entfernt werden

# lösche bitte + Name des Dictionaries["Schlüssel zum genauen Eintrag der gelöscht werden soll angeben"]
del hund["lieblingsessen"]
# del -> delete = löschen

for schluessel, wert in hund.items():
    print(schluessel, ":", wert)
    
# 5) Prüfen ob ein Schlüssel existiert
# IHK WICHTIG: Man soll ja Fehler vermeiden

if "name" in hund:
    print(hund["name"])
else:
    print("Kein Name wurde gefunden!")