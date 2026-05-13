# Projekt-Aufgabe: Der Tempel der Weisheit
#
# Erstelle ein Zelda-ähnliches Abenteuer.
#
# Nutze:
# - if
# - elif
# - else
# - nested ifs
#
# Anforderungen:
#
# 1. Frage den Namen des Helden ab.
# 2. Frage die Anzahl der Herzen ab.
# 3. Frage die Anzahl der Schlüssel ab.
#
# Wenn Herzen unter 5:
# Ausgabe -> "Du bist zu schwach für den Tempel."
#
# Wenn Herzen zwischen 5 und 11:
# Ausgabe -> "Du darfst den ersten Raum betreten."
#
# Wenn Herzen ab 12:
# Ausgabe -> "Du darfst den Bossraum betreten."
#
# 4. Nur wenn Herzen ab 12 sind:
#    Frage, ob der Masterschlüssel vorhanden ist: ja/nein
#
#    Wenn ja:
#    Ausgabe -> "Die Boss-Tür öffnet sich."
#
#    Wenn nein:
#    Ausgabe -> "Die Boss-Tür bleibt verschlossen."
#
# 5. Frage nach dem Item:
#    - Schwert
#    - Bumerang
#    - Bogen
#
# 6. Je nach Item soll ein anderes Rätsel gelöst werden.
#
# Bonus:
# Wenn Schlüssel ab 3 sind:
#     Ausgabe -> "Du kannst geheime Räume öffnen."
#
# Ziel:
# Baue Rätsel, Kämpfe und mehrere Enden ein.

herzen = int(input("Willkommen zu deinem Zelda-Abenteuer! Gib die Anzahl deiner Herzen ein um fortzufahren: "))

if herzen < 5:              # Wenn Herzen unter 5:
    print("Du bist zu schwach für den Tempel.")
elif 5 <= herzen < 12:      # Wenn Herzen zwischen 5 und 11:
    print("Du darfst den ersten Raum betreten.")
else:                       # Wenn Herzen ab 12:
    print("Du darfst den Bossraum betreten.")
    masterschluessel = input("Hast du den Masterschlüssel? (ja/nein): ")
    if masterschluessel.lower() == "ja":        # Input ja
        print("Die Boss-Tür öffnet sich.")
    else:                                       # Input nein (nicht ja)
        print("Die Boss-Tür bleibt verschlossen.")

item = input("Welches Item hast du als letztes erhalten (Schwert/Bumerang/Bogen)?: ")
if item.lower() == "schwert":
    print("Du musst den 1. Schlüssel findenum weiterzukommen!")
elif item.lower() == "bumerang":
    print("Du musst den 2. Schlüssel findenum weiterzukommen!")
elif item.lower() == "bogen":
    print("Du musst den 3. Schlüssel findenum weiterzukommen!")
else:
    print("Ungültiges Item!")
schluessel = int(input("Wie viele Schlüssel hast du?: "))
if schluessel >= 3:
    print("Du kannst geheime Räume öffnen.")