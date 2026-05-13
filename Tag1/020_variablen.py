# Variablen
# ... speichert Informationen. Ist wie ein Behälter bzw. eine Kiste, die den Inhalt verwaltet.

tier = "Hund"
# tier -> Name der Variable
# = -> sagt mir "Speichere"
# "Hund" -> gespeicherte Wert in meiner Variable

print(tier)

# STRING -> Text
# Texte nennt man in Python String
tiername = "Bello"
print(tiername)

tierart = "Katze"
name = "Poupette"
farbe = "rot"

print(tierart)
print(name)
print(farbe)


# Zahlen können auch Strings sein, aber sie müssen in Anführungszeiche stehen
alter = "34"
print(alter)

############################################################################

# INTEGER -> ganze Zahlen
# int = abkürzung für Integer

anzahl_beine = 4
punkte = 100
name = "Ulf"
farbe = "Blau"
print (name)
print (farbe)

print(anzahl_beine, punkte)

jahr = 2026

print(jahr + 5)
print(jahr - 10)
print(jahr * 3)

# Integer kann positiv, negativ oder 0 sein
bayern = 0
temperatur = -15

print(bayern, temperatur)

############################################################################

# FLOAT -> Kommazahlen
# ... ist eine Zahl die eine Nachkommastelle hat. In Pyhton schreiben wir kommazahlen mit Punkt statt mit Komma.

gewicht = 85
groesse = 1.90
preis = 2.59

# gewicht = 25,6  # das wären zwei Werte (Tuple)


bmi = gewicht / (groesse * groesse)# Formel für den Body Mass Index
print(bmi)
untergewicht = 18.5
übergewicht = 25

print("Untergewicht ab " + str(untergewicht* groesse * groesse) + " Kilogramm")
print("Übergewicht ab " + str(übergewicht* groesse * groesse) + " Kilogramm")

# Ganze Zahlen können mit Kommazahlen verrechnet werden, das Ergebnis ist dann eine Kommazahl
print(gewicht + groesse)

# BOOLEAN -> Wahrheitswert
# bool = Boolean
# bool hat zwei Werte: True (wahr) und False (falsch)

ist_hund = True
ist_katze = False

print(ist_hund) # True
print(ist_katze) # False

# Datentyp prüfen -> type()

name_hund = "Mousse"
alter_hund = 5
gewicht_hund = 25.6
ist_hund = True

print(type(name_hund)) # Gibt den typ der Variable name_hund aus (str)
print(type(alter_hund)) # Gibt den typ der Variable alter_hund aus (int)
print(type(gewicht_hund)) # Gibt den typ der Variable gewicht_hund aus (float)
print(type(ist_hund)) # Gibt den typ der Variable ist_hund aus (bool)