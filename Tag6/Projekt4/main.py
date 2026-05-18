# Kommentar zu JSON

# Schlüssel müssen in doppelten Anführungszeichen stehen
# Strings müssen in doppelten Anführungszeichen stehen
# Keine Kommas am Ende ENDE
# true, false, null werden klein geschrieben

import json         # Python hat ein eingebautes Modul

# um die JSON lesen zu können, müssen wir im Ordner Projekt 4 drin sein!
# LF05 ... cd Tag6... cd Projekt4
with open("daten.json", "r") as datei:   # mit open() öffnen wir die Datei, damit wir sie lesen können
    daten = json.load(datei)
    
    print (daten["name"])    # Ausgabe: Mousse
    
# Überschreibt die schon vorhandenden Daten in unserer JSON Datei
daten = {
    "rasse": "Carpatin",
    "art" : "Hund"
}

with open("daten.json", "w") as datei:      #w -> write bedeutet schreiben
    json.dump(daten, datei)                 # dump() -> damit schreiben wir die Daten in die Datei (reinwerfen, ablegen)

# # Neuen Daten
# neuer_eintrag = [
#     {
#         "character": "DIVA",
#         "freundlichkeit": "99 Prozent genervt von allem und jedem"
#     }
# ]

# # Daten anhängen
# daten.update(neuer_eintrag)

# # Speicher
# with open("daten.json", "w") as datei:
#     json.dump(daten, datei, indent=6)
    