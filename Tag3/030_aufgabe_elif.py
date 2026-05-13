# Aufgabe: Zauberprüfung
#
# Frage den Schüler nach seiner Punktzahl.
#
# Regeln:
#
# Ab 90:
# Ausgabe -> Du wirst Vertrauensschüler
#
# Ab 60:
# Ausgabe -> Prüfung bestanden
#
# Unter 60:
# Ausgabe -> Nachsitzen bei Snape
#
# Nutze:
# if / elif / else

punkte = int(input("Bitte gib deine Punktzahl ein: "))
if punkte >= 90:
    print("Du wirst Vertrauensschüler!")
elif punkte >= 60:
    print("Prüfung bestanden!")
else:
    print("Nachsitzen bei Snape!")
    
# Aufgabe: Tor von Moria
#
# Frage den Spieler nach seiner Stärke.
#
# Regeln:
#
# Ab 100:
# Ausgabe -> Das Tor öffnet sich
#
# Ab 50:
# Ausgabe -> Die Wachen beobachten dich
#
# Unter 50:
# Ausgabe -> Du wirst zurückgeschickt
#
# Nutze:
# if / elif / else

staerke = int(input("Bitte gib deine Stärke ein: "))
if staerke >= 100:
    print("Das Tor öffnet sich!")
elif staerke >= 50:
    print("Die Wachen beobachten dich!")
else:
    print("Du wirst zurückgeschickt!")

# Aufgabe: Arena-Challenge
#
# Frage den Trainer nach der Anzahl seiner Orden.
#
# Regeln:
#
# Ab 8:
# Ausgabe -> Pokémon Liga freigeschaltet
#
# Ab 4:
# Ausgabe -> Du darfst stärkere Arenen betreten
#
# Unter 4:
# Ausgabe -> Trainiere weiter
#
# Nutze:
# if / elif / else

orden = int(input("Bitte gib die Anzahl deiner Orden ein: "))
if orden >= 8:
    print("Pokémon Liga freigeschaltet!")
elif orden >= 4:
    print("Du darfst stärkere Arenen betreten!")
else:
    print("Trainiere weiter!")
    
# Aufgabe: Zombie-Apokalypse
#
# Frage nach der Anzahl der Vorräte.
#
# Regeln:
#
# Ab 100:
# Ausgabe -> Basis gesichert
#
# Ab 50:
# Ausgabe -> Vorräte werden knapp
#
# Unter 50:
# Ausgabe -> Gefahr! Nahrung fast leer
#
# Nutze:
# if / elif / else

vorräte = int(input("Bitte gib die Anzahl deiner Vorräte ein: "))
if vorräte >= 100:
    print("Basis gesichert!")
elif vorräte >= 50:
    print("Vorräte werden knapp!")
else:
    print("Gefahr! Nahrung fast leer!")
    
# Aufgabe: Firewall-Check
#
# Frage nach der Sicherheitsstufe eines Systems.
#
# Regeln:
#
# Ab 90:
# Ausgabe -> System maximal gesichert
#
# Ab 60:
# Ausgabe -> Mittlere Sicherheit
#
# Unter 60:
# Ausgabe -> System gefährdet
#
# Nutze:
# if / elif / else

sicherheitsstufe = int(input("Bitte gib die Sicherheitsstufe ein: "))
if sicherheitsstufe >= 90:
    print("System maximal gesichert!")
elif sicherheitsstufe >= 60:
    print("Mittlere Sicherheit!")
else:
    print("System gefährdet!")

# Aufgabe: Serverraum
#
# Frage nach der CPU-Auslastung.
#
# Regeln:
#
# Unter 50:
# Ausgabe -> Server läuft stabil
#
# Zwischen 50 und 80:
# Ausgabe -> Hohe Auslastung erkannt
#
# Über 80:
# Ausgabe -> Warnung: Server überlastet
#
# Nutze:
# if / elif / else

cpu_auslastung = int(input("Bitte gib die CPU-Auslastung ein: "))
if cpu_auslastung < 50:
    print("Server läuft stabil!")
elif cpu_auslastung <= 80:
    print("Hohe Auslastung erkannt!")
else:
    print("Warnung: Server überlastet!")

# Aufgabe: Tierheim-Verwaltung
#
# Frage nach der Anzahl freier Plätze.
#
# Regeln:
#
# Ab 20:
# Ausgabe -> Viele Plätze verfügbar
#
# Ab 5:
# Ausgabe -> Noch einige Plätze frei
#
# Unter 5:
# Ausgabe -> Tierheim fast voll
#
# Nutze:
# if / elif / else

freie_plaetze = int(input("Bitte gib die Anzahl freier Plätze ein: "))
if freie_plaetze >= 20:
    print("Viele Plätze verfügbar!")
elif freie_plaetze >= 5:
    print("Noch einige Plätze frei!")
else:
    print("Tierheim fast voll!")
    
# Aufgabe: Tempel-Zugang
#
# Frage nach der Anzahl gesammelter Herzen.
#
# Regeln:
#
# Ab 15:
# Ausgabe -> Meistertempel betreten
#
# Ab 8:
# Ausgabe -> Neue Regionen freigeschaltet
#
# Unter 8:
# Ausgabe -> Du brauchst mehr Herzen
#
# Nutze:
# if / elif / else

herzen = int(input("Bitte gib die Anzahl gesammelter Herzen ein: "))
if herzen >= 15:
    print("Meistertempel betreten!")
elif herzen >= 8:
    print("Neue Regionen freigeschaltet!")
else:
    print("Du brauchst mehr Herzen!")
    
# Aufgabe: Passwort-Knacker
#
# Frage nach der Anzahl geknackter Verschlüsselungen.
#
# Regeln:
#
# Ab 50:
# Ausgabe -> Elite-Hacker erkannt
#
# Ab 20:
# Ausgabe -> Fortgeschrittener Hacker
#
# Unter 20:
# Ausgabe -> Anfänger entdeckt
#
# Nutze:
# if / elif / else

erfolgreiche_hacks = int(input("Bitte gib die Anzahl geknackter Verschlüsselungen ein: "))
if erfolgreiche_hacks >= 50:
    print("Elite-Hacker erkannt!")
elif erfolgreiche_hacks >= 20:
    print("Fortgeschrittener Hacker!")
else:
    print("Anfänger entdeckt!")
    
    
# Aufgabe: Abenteuer im Dungeon
#
# Frage den Spieler nach seiner Anzahl an Goldmünzen.
#
# Regeln:
#
# Ab 100:
# Ausgabe -> Du kaufst ein legendäres Schwert
#
# Ab 50:
# Ausgabe -> Du kaufst eine bessere Rüstung
#
# Unter 50:
# Ausgabe -> Du kannst dir nur einen Heiltrank leisten
#
# Nutze:
# if / elif / else

gold = int(input("Bitte gib die Anzahl deiner Goldmünzen ein: "))
if gold >= 100:
    print("Du kaufst ein legendäres Schwert!")
elif gold >= 50:
    print("Du kaufst eine bessere Rüstung!")
else:
    print("Du kannst dir nur einen Heiltrank leisten!")
