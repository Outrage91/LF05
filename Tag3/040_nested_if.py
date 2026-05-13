# Nested if
# ... eine Entscheidung passiert innerhalb einer anderen Entscheidung

hund_hunger = True
futter_da = True

if (hund_hunger):
    print("Bello hat Hunter!")
    if (futter_da):
        print("Bello bekommt Futter!")
    else:
        print("Oh oh... wir haben kein Futter mehr!")
else:
    print("Bello schläft!")
    
# Hat Bello Hunger?
# |
# ├── Nein -> Bello schläft
# |
# └── Ja
#     |
#     └── Gibt es Futter?
#     |
#     ├── Ja -> Bello bekommt Futter
#     └── Nein -> Bello ist beleidigt

# IHK WICHTIG:
# Nested if -> bedeutet doppelte Einrückung -> Codeblock innerhalb eines Codeblocks

# Else gehört immer zu dem if auf derselben Einrückungsebene!

katze_wach = True
katze_zerstoert_tastatur = False

if katze_wach:
    print("Die Katze ist wach!")
    if not katze_zerstoert_tastatur:        # not = verneinung/ Gegenteil
        print("Die Katze darf ins Büro!")
    else:
        print("Die Katze hat Hausverbot!")
else:
    print("Die Katze schläft auf dem Scanner!")
    
papagei_freundlich = True
beleidigt_besucher = True

if papagei_freundlich:
    print("Der Papagei bereit für die Besucher!")
    if not beleidigt_besucher:
        print("Die Besucher dürfen eintreten!")
    else:
        print("Der Papagei wird heute ignoriert!")
else:
    print("Der Papagei schreit unser WLAN-Passwort in Dauerschleife!")
    

# IHK WICHTIG:

# Bedingte Anweisung (if)
# Eine if-Anweisung ist eine Verzweigung bzw. Kontrollstruktur,
# mit der ein Programm entscheidet, ob ein Codeblock ausgeführt werden soll.
# Der Codeblock wird ausgeführt, wenn die Bedingung den Wert True hat.

# if bedingung:
#   anweisung

# Bedingung
# ... Ausdruck mit True (wahr) oder False (falsch)

# Kontrollstruktur
# ... Steuert unseren Programmablauf

# Codeblock
# ... Zusammenhängiger eingerückter Code

# Alternativzwei (else)
# ... else definiert einen alternativen Codeblock, der ausgeführt wird, wenn die Bedingung der vorherigen
#     if-Anweisung falsch (false) ist.

# if bedingung:
#   anweisung
# else:
#   alternative_anweisung

# - else besitzt KEINE eigene Bedingung
# - else IMMER immer zu dem if auf derselben Einrückungsebene -> immer zu EINEM vorherigen if
# - Es wird immer genau EINER der beiden Blöcke ausgeführt -> entweder der if-Block oder der else-Block, niemals beide gleichzeitig

# Erweiterte Verzweigung (elif = else if = elsif in anderen Sprachen)
# elif steht für "else if" und ermöglicht die Prüfung weiterer Bedigungen, wenn vorherige Bedingungen falsch waren. (Es können beliebig viele elif-Blöcke verwendet werden, um verschiedene Szenarien abzudecken).
# Damit können mehrere Entscheidungswege abgebildet werden.

# if bedingung1:
#    anweisung1
# elif bedingung2:
#    anweisung2
# else:
#    alternative_anweisung

# IHK WIHCTIG
# Bedingungen werden von oben nach unten geprüft
# Sobald eine Bedingung wahr ist -> werden die restlichen Bedingungen übersprungen
# Es können beliebig viele elif verwendet werden

# Verschachtelte Verzweigung (Nested-if)
# Ein "nested if" ist eine verschachtelte if-Anweisung innerhalb einer anderen if-Anweisung.
# Sie wird verwendet, wenn nach einer ersten Entscheidung weitere Bedingungen geprüft werden müssen.

# if bedingung1:
#   if bedingung2:
#       anweisung

# Die innerer Bedingung wird nur geprüft, wenn die äußere Bedingung erfüllt wurde.