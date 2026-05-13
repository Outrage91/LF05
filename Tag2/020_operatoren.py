# Operatoren

#Addition mit +
hund = 3
katze = 2

alle_tiere = hund + katze   # 3 + 2
print(alle_tiere)           # Ergebnis = 5

# links steht die Variable (alle_tiere), rechts steht die Operation (hund + katze)

kaninchen = 4
alle_tiere = hund + katze + kaninchen   # 3 + 2 + 4
print(alle_tiere)                       # Ergebnis = 9

#######################################################################################

# Subtraktion mit -
katzen = 10
vermittelt = 3
uebrig = katzen - vermittelt    # 10 - 3
print(uebrig)                   # Ergebnis = 7

hunde = 12
vermittelt = 5
uebrig = hunde - vermittelt     # 12 - 5
print(uebrig)                   # Ergebnis = 7

###########################################################################################

# Multiplikation mit *
# in Python rechnen wir bei Multiplikation immer mit Sternchen (*) nicht mit x

hunde = 4
leckerlis_pro_hund = 3
gesamt_leckerlis = hunde * leckerlis_pro_hund    # 4 * 3 (3 + 3 + 3 + 3)
print(gesamt_leckerlis)                          # Ergebnis = 12

#############################################################################################

# Division mit /

dosen = 42
hunde = 23

pro_hund = dosen / hunde     # 42 / 23
print(pro_hund)              # Ergebnis = 1.8260869565217392
type(pro_hund)               # Ergebnis = <class 'float'> -> Kommazahl


dosen = 18
katzen = 6

pro_katze = dosen / katzen      # 18 / 6
print(pro_katze)                # Ergebnis = 3.0

##############################################################################################

# Modulo mit % 
# Modulo fragt: "Was bleibt übrig, wenn ich die erste Zahl durch die zweite Zahl teile? 

hunde = 13

rest = hunde % 5     # 13 / 5 -> 2, Rest = 3
print(rest)          # Ergebnis = 3

# Was passiert hier
# Aufgabe: Wir hatten 13 Hunde und diese sollen in Gruppen eingeteilt werden, wobei jede Gruppe 5 Tiere umfasst.
# Lösung:   1. Runde: 5 Hunde in Gruppe 1 (8 Hunde übrig)
#           2. Runde: 5 Hunde in Gruppe 2 (3 Hunde übrig)
#           3. Runde: 3 Hunde in Gruppe 3 (0 Hunde übrig)

katzen = 69

rest = katzen % 15    # 69 / 15 -> 4, Rest = 9
print (rest)          # Ergebnis = 9

###########################################################################################
# Potenz mit **
# ** bedeutet Potenz (mal sich selbst)
# 2^4 wird in Python nicht akzeptiert, sondern 2 ** 4

kaninchen = 2 ** 4   # 2 * 2 * 2 * 2

print(kaninchen)    # Ergebnis = 16

###########################################################################################

num = 2 + 3 * 4     # Rechenweg 3 *4 = 12, dann 2 + 12 = 14
print(num)          # Ergebnis = 14, weil Multiplikation vor Addition gerechnet wird 

num1 = (2 + 3) * 4  # Klammern haben Vorrang, deshalb wird zuerst 2 + 3 gerechnet und dann mit 4 multipliziert
print(num1)         # Ergebnis = 20, weil Klammern Vorrang haben

num2 = 8 / 2 * 3   # Rechenweg 8 / 2 = 4, dann 4 * 3 = 12
print(num2)         # Ergebnis = 12, weil Division und Multiplikation den gleichen Vorrang haben, deshalb wird von links nach rechts gerechnet

num3 = 2 * 3 / 8   # Rechenweg 2 * 3 = 6, dann 6 / 8 = 0.75
print(num3)         # Ergebnis = 0.75, weil Multiplikation und Division den gleichen Vorrang haben, deshalb wird von links nach rechts gerechnet

# Wir rechnen IMMER bei gleicher Priorität von LINKS nach RECHTS!

num4 = 2 ** 3 ** 2   # Rechenweg 3 ** 2 = 9, dann 2 ** 9 = 512
print(num4)          # Ergebnis = 512, weil Potenz den höchsten Vorrang hat ( RECHTS nach LINKS - rechtsassoziativ)
