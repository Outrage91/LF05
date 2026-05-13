# Variante 1
name = "Vic"
print("Hallo " + name)

# Variante 2
# alter = 32
#print("Ich bin " + alter + " Jahre alt!" -> Datentypen stimmen nicht überein, weil alter eine Zahl ist und ich versuche sie mit einem String zu verbinden. Das funktioniert nicht, weil Python nicht weiß, wie es die Zahl in einen String umwandeln soll.

alter = 32
print("Ich bin " + str(alter) + " Jahre alt!")

# Variante 3 -> f-string
# alter bezieht sich auf die Variable von Variante 2

print(f"Ich bin {alter} Jahre alt!")

# f vor dem String bedeutet in diesem Text dürfen Variablen (unterschiedliche Datentypen) eingesetzt werden.
# f = formatted (formatted string literal = formatierter String)

print(f"Hallo mein Name ist {name}. Ich bin {alter} Jahre alt!")