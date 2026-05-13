# Aufgabe: Das Herr-der-Ringe-Verwaltungssystem

# In Mittelerde herrscht heute Chaos.
# Schreibt ein Python-Programm, das der Gemeinschaft hilft.

# 1. Speichert folgende Dinge in Variablen:
# - 6 Hobbits
hobbit1 = "Frodo"
hobbit2 = "Sam"
hobbit3 = "Merry"
hobbit4 = "Pippin"
hobbit5 = "Bilbo"
hobbit6 = "Ohm Gamdschie"
# - 4 Elben
elbe1 = "Legolas"
elbe2 = "Arwen"
elbe3 = "Galadriel"
elbe4 = "Elrond"
# - 3 Zwerge
zwerg1 = "Gimli"
zwerg2 = "Thorin"
zwerg3 = "Balin"

# 2. Berechnet:
# Wie viele Gefährten insgesamt in Mittelerde unterwegs sind.
# Benutzt den Operator: +

# Anzahl Gefährten = Anzahl Hobbits + Anzahl Elben + Anzahl Zwerge

# Anzahl Hobbits = 6

hobbits = [hobbit1, hobbit2, hobbit3, hobbit4, hobbit5, hobbit6]
anzahl_hobbits = len(hobbits)
# Anzahl Elben = 4 

elben = [elbe1, elbe2, elbe3, elbe4]
anzahl_elben = len(elben)
# Anzahl Zwerge = 3

zwerge = [zwerg1, zwerg2, zwerg3]
anzahl_zwerge = len(zwerge)

anzahl_gefaehrten = anzahl_hobbits + anzahl_elben + anzahl_zwerge
print(f"Anzahl Gefährten: {anzahl_gefaehrten}")
# 3. Getrennte Gefährten
# 5 Gefährten werden auf der Reise getrennt.
# Berechnet:
# Wie viele Gefährten noch zusammenbleiben.
# Benutzt den Operator: -
anzahl_zusammen = anzahl_gefaehrten - 5
print(f"Es verbleiben {anzahl_zusammen} Gefährten zusammen.")

# 4. Lembas-Brote berechnen
# Jeder Gefährte bekommt 3 Lembas-Brote.
# Berechnet:
# Wie viele Lembas-Brote insgesamt benötigt werden.
# Benutzt den Operator: *

anzahl_lembas = anzahl_gefaehrten * 3
print(f"Es werden insgesamt {anzahl_lembas} Lembas-Brote benötigt.") # Ausgabe: Es werden insgesamt 39 Lembas-Brote benötigt.

# 5. Lembas-Brote gerecht verteilen
# Berechnet:
# Wie viele Lembas-Brote jeder Gefährte bekommt.
# Benutzt den Operator: /
anzahl_lembas_brote = int(input("Wie viele Lembas-Brote werden verteilt? "))
anzahl_lembas_pro_gefaehrte = anzahl_lembas_brote // anzahl_gefaehrten
anzahl_lembas_pro_gefaehrte2 = anzahl_lembas_brote / anzahl_gefaehrten
print(f"Jeder Gefährte bekommt {anzahl_lembas_pro_gefaehrte} Lembas-Brote.")
print(f"Jeder Gefährte bekommt {int(round(anzahl_lembas_pro_gefaehrte2, 0))} Lembas-Brote.")

# 6. Rest berechnen
# Die Lembas-Brote werden in 5er-Päckchen verpackt.
# Berechnet:
# Wie viele Lembas-Brote übrig bleiben.
# Benutzt den Operator: %
rest_lembas = anzahl_lembas_brote % 5
print(f"Es bleiben {rest_lembas} Lembas-Brote übrig.")

# 7. Magische Ringkraft
# Berechnet:
# 2 ** 3
# Was kommt dabei heraus?
# Benutzt den Operator: **
int1 = 2
int2 = 3
ringkraft = int1 ** int2
print(f"2^3 = {ringkraft}") # Ausgabe: 8 = 2 * 2 * 2

# Wichtige Hinweise:
# - Benutzt Variablen
# - Nutzt print() für die Ausgabe
# - Führt euer Programm nach jedem Schritt aus
# - Achtet auf die richtige Schreibweise der Operatoren

# Bonus:
# Testet eigene Zahlen
# Testet Klammern
# Testet round() für Kommazahlen
 