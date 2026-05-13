# Aufgabe:
# Schreibe ein Programm, das den Benutzer nach einem Passwort fragt.
#
# Wenn das Passwort richtig ist:
# Ausgabe -> Zugang erlaubt
#
# Wenn das Passwort falsch ist:
# Ausgabe -> Falsches Passwort

eingabe = input("Bitte gib das Passwort ein: ")
passwort = "gutespasswort123"

if eingabe == passwort:
    print("Zugang erlaubt!")
else:
    print("Falsches Passwort!")