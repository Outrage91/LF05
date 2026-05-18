# Einfaches einlesen

datei = open("text.txt", "r")
# open()
# 1) sucht die Datei
# 2) öffnet sie im Betriebssystem
# 3) reserviert Speicher
# 4) erstellt ein Dateiobjekt (eine Variable, die Infos über die Datei enthält)

# text.txt
# ... das ist der Dateiname
# -> sucht wo liegt text.txt

# r
# -> nennen wir Modus
# r steht für read -> bedeutet zu deutsch lesen

inhalt = datei.read()
# read()
# Python liest ALLES aus der Datei

# Der komplette Inhalt wird von der Festplatte in den Arbeitsspeicher geladen
# -> liefer IMMER einen String
print(inhalt)

datei.close
# close
# damit wird unsere Verbindung zur Datei beendet.