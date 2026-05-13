# Vergleichsoperatoren

# IHK WICHTIG:
# - Ein Vergleich ergibt IMMER einen Wahrheitswert (Boolean: True oder False).
# - True bedeutet wahr, False bedeutet falsch.
# - Vergleichsoperatoren werden oft in if-Bedingengungen verwendet, um Entscheidungen zu treffen.

# 1) Gleichheit ==
# == prüft ob zwei Werte gleich sind.

tier = "Hund"

print (tier == "Hund") # Ausgabe: True, weil tier den Wert "Hund" hat
print (tier == "Katze") # Ausgabe: False, weil tier den Wert "Hund

# 2) Ungleich !=
# != prüft ob zwei Werte unterschiedlich sind.

tier = "Katze"
print (tier != "Hund") # Ausgabe: True, weil tier den Wert "Katze" hat
print (tier != "Katze") # Ausgabe: False, weil tier den Wert "Katze" hat

# 3) Größer als >
# > prüft ob der linke Wert größer ist als der rechte Wert.

gewicht = 12

print(gewicht > 10) # Ausgabe: True, weil 12 größer ist als 10
print(gewicht > 25) # Ausgabe: False, weil 12 nicht größer ist als 25

# IHK WICHTIG:
# Bei Zahlenvergleichen ist wichtig das in Python die Werte verglichen werden, nicht die Variablennamen!

# 4) Kleiner als <
# < prüft ob der linke Wert kleiner ist als der rechte Wert.

leckerlis = 3

print(leckerlis < 5) # Ausgabe: True, weil 3 kleiner ist als 5
print(leckerlis < 2) # Ausgabe: False, weil 3 nicht kleiner ist als 2

# 5) Größer oder gleich >=
# >= prüft ob der linke Wert größer oder gleich ist als der rechte Wert.

alter = 18

print(alter >= 18) # Ausgabe: True, weil 18 größer oder gleich 18 ist
print(alter >= 17) # Ausgabe: True, weil 18 größer oder gleich 17 ist
print(alter >= 28) # Ausgabe: False, weil 18 nicht größer oder gleich 28 ist

# IHK WICHTIG:
# Viele vergessen das "oder gleich". > bedeutet größer! >= bedeutet größer oder gleich!

# 6) Kleiner oder gleich <=
# <= prüft ob der linke Wert kleiner oder gleich ist als der rechte Wert.

temperatur = 0
print(temperatur <= 0) # Ausgabe: True, weil 0 kleiner oder gleich 0 ist
print(temperatur <= 5) # Ausgabe: True, weil 0 kleiner oder gleich 5 ist
print(temperatur <= -3) # Ausgabe: False, weil 0 nicht kleiner oder gleich -3 ist

# IHK WICHTIG:
# "Hund" ist nicht dasselbe wie "hund". Groß- und Kleinschreibung ist wichtig bei Vergleichen von Texten! (Case-Sensitivity)
# Pythan ist da sehr genau!

print ("Hund" == "hund") # Ausgabe: False, weil "Hund" nicht dasselbe ist wie "hund"

# IHK WICHTIG:
# Operator in der richtigen Reihenfogle schreiben
# <= -> RICHTIG | =< -> FALSCH

# Vergleichsoperator
# ... Operator zum Vergleichen von Werten.

# Boolean
# ... Datentyp mit True oder False

# Operand
# ... Wert links oder rechts vom Operator

# Ausdruck
# ... Kombination aus Werten, Variablen und Operatoren.