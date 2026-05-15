# -----------------------------------
# Aufgabe 1 — While-Schleife
# Thema: Mana aufladen
# -----------------------------------

# Schreibe ein Programm:
#
# - Der Spieler startet mit 0 Mana
mana = 0
# - Solange das Mana kleiner als 100 ist:
while mana < 100:
#     - soll "Mana wird aufgeladen..." ausgegeben werden
    print("Mana wird aufgeladen...", mana)
#     - das Mana soll um 20 erhöht werden
    mana+=20
# - Wenn das Mana voll ist:
#     - soll "Zauber bereit!" ausgegeben werden
print("Zauber bereit!")
# -----------------------------------
# Aufgabe 2 — For-Schleife
# Thema: Dungeon
# -----------------------------------

# Schreibe ein Programm:
#
# - Die Schleife soll 5-mal laufen
# - Bei jedem Durchlauf:
#     - "Gegner wurde besiegt" ausgeben
# - Nach der Schleife:
#     - "Dungeon abgeschlossen" ausgeben
#

for i in range(5):
    print("Gegner", i+1, "wurde besiegt!")
print("Dungeon abgeschlossen")

# Bonus:
# - Gib zusätzlich die Nummer des Gegners aus
#   Beispiel:
#   Gegner 1 wurde besiegt
#   Gegner 2 wurde besiegt

# Eine Funktion, die zwei Zahlen addiert
def addieren(zahl1, zahl2):
    print(zahl1+zahl2)
    return zahl1 + zahl2

addieren(4, addieren(3, 7))