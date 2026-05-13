# Input() Funktion

name = input("Wie heißt dein Hund? ")
print(name)

# input() gibt mir immer Text zurück, auch wenn der Benutzer eine Zahl eingibt. Das bedeutet, dass die Variable "alter" in diesem Fall ein String ist, auch wenn der Benutzer eine Zahl eingibt.

# Variante 1
alter= input("Wie alt bist du? ")
print(type(alter))
alter = int(alter)

print(alter)

# Schritt 1: Python zeigt uns die Frage = Wie alt bist du?
# Schritt 2: User gibt sein Alter ein, z.B. 34
# Schritt 3: input() Funktion gibt den Text "34" zurück, weil input() immer Text zurückgibt
# Schritt 4: alter = int(alter) -> bedeutet der Text "34" wird in eine Zahl umgewandelt, damit wir damit rechnen können. 
# -> Jetzt ist alter eine Integer Variable und kein String mehr.
# Schritt 5: Ausgabe des Alters = 34
# Schritt 6: kann mit alter jetzt weiter rechnen
print(alter + 5)

# Variante 2
neu_alter = int(input("Wie alt bist du? "))
print(type(neu_alter))
print(neu_alter)