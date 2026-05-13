import random
# Um das random Modul zu verwenden, muss es importiert werden -> import random

zahl = random.randint(1, 6) # randint -> random integer -> Zufallszahl zwischen 1 und 6 (Würfel)

print("Die gewürfelte Zahl ist:",zahl)

# randint(a, b) -> gibt eine zufällige Ganzzahl N zurück, die a <= N <= b erfüllt. (inklusive a und b)
# beide Grenzen sind mit eingeschlossen
# a steht für die kleinste Zahl
# b für die größte Zahl
# wird nur für ganze Zahlen genutzt und gibt zufällig eine Zahl zwischen a und b zurück (a und b eingeschlossen)

hund_num = random.randint(1, 10)

print(f"Hund Nr. {hund_num} bekommt ein Leckerli!")

#uniform()

gewicht = random.uniform(2.7, 12.8)

print(f"Die Katze wiegt momentan {gewicht} kg!")
print(f"Die Katze wiegt momentan {round(gewicht, 2)} kg!")

#uniform(a, b)
# gibt eine zufällige Fließkommazahl N zurück, die a <= N <= b erfüllt. (inklusive a und b)
# beide Grenzen sind mit eingeschlossen
# a steht für die kleinste Zahl
# b für die größte Zahl

# randrange(start, stop, schritte)
# start -> da wo wir beginnen
# stop -> da wo wir aufhören
# schritt -> In welchen Abständen gezählt wird
# stop Zahl ist NICHT mit dabei in der Ausgabe

zahlen = random.randrange(0, 10, 2) # gibt eine zufällige Zahl zwischen 0 und 10 (nicht inklusive) zurück, die durch 2 teilbar ist (0, 2, 4, 6, 8)

print(zahlen)

# triangular(start, stop, mode) --- Dreiecksverteilung um den Wert mode herum

katzenfutter = random.triangular(1, 100, 70)
print(f"Die Katze bekommt {round(katzenfutter, 2)} Gramm Futter!")