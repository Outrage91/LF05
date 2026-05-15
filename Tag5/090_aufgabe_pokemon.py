# =====================================================
# DAS POKÉMON-FUNKTIONSLABOR
#
# Ziel:
# Trainiere Funktionen mit Pokémon-Kämpfen.
# =====================================================


# =====================================================
# AUFGABE 1
# TRAINER-BEGRÜSSUNG
#
# Erstelle eine Funktion:
#
# begruessung()
#
# Ausgabe:
#
# "Willkommen im Pokémon-Center!"
# =====================================================



# =====================================================
# AUFGABE 2
# TRAINER STARTEN
#
# Erstelle eine Funktion:
#
# begruesse_trainer(name)
#
# Beispiel:
#
# "Hallo Ash, bereit für den Arenakampf?"
# =====================================================
def begruesse_trainer(name):
    print("Hallo", name + ", bereit für den Arenakampf?")
begruesse_trainer("Ash")



# =====================================================
# AUFGABE 3
# ATTACKEN-SYSTEM
#
# Erstelle eine Funktion:
#
# berechne_attacke(attacke, bonus)
#
# Die Funktion soll:
#
# attacke + bonus
#
# berechnen und zurückgeben.
# =====================================================


# =====================================================
# AUFGABE 4
# SEHR EFFEKTIV
#
# Falls die Attacke über 20 liegt:
#
# "Sehr effektiver Treffer!"
# =====================================================
def berechne_attack(attacke, bonus):
    gesamt = attacke + bonus
    if attacke > 20:
        print("Sehr effektiver Treffer!")
    return gesamt
print("Gesamtschaden:", berechne_attack(25, 10))



# =====================================================
# AUFGABE 5
# RUCKSACK-CHECK
#
# Prüfe mit einer Funktion,
# ob ein bestimmtes Item
# im Rucksack existiert.
#
# Beispiele:
#
# "Pokeball"
# "Trank"
# "Top-Beleber"
# =====================================================

def check_rucksack(item, rucksack):
    if item in rucksack:
        print(item, "ist im Rucksack!")
    else:
        print(item, "ist nicht im Rucksack.")
check_rucksack("Pokeball", ["Trank", "Top-Beleber", "Pokeball"])



# =====================================================
# AUFGABE 6
# ORDEN SAMMELN
#
# Erstelle eine Funktion,
# die die Anzahl der Orden erhöht.
# =====================================================

aktuelle_orden = 3
def orden_erhalten():
    neue_orden = aktuelle_orden + 1
    print("Du hast einen neuen Orden erhalten! Gesamtorden:", neue_orden)
    return neue_orden
orden_erhalten()
orden_erhalten()
aktuelle_orden = orden_erhalten()
aktuelle_orden = orden_erhalten()



# =====================================================
# AUFGABE 7
# ARENAKAMPF
#
# Falls die Attacke >= 50:
#
# "Der Arenaleiter wurde besiegt!"
#
# Sonst:
#
# "Das gegnerische Pokémon kämpft weiter!"
# =====================================================

def arenakampf(attacke):
    if attacke >= 50:
        print("Der Arenaleiter wurde besiegt!")
    else:
        print("Das gegnerische Pokémon kämpft weiter!")
arenakampf(40)
arenakampf(100)