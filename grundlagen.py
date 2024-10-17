dollarkurs = float(input("Dollarkurs: "))
kapital_in_euro = round(float(input("Kapital in Euro: ")), 2)
wechselgebühr = float(input("Wechselgebühr: "))
endbetrag = kapital_in_euro * dollarkurs * (1 - wechselgebühr)

print(f"\nAnfangskapital in Euro: {kapital_in_euro}")
print(f"Dollarkurs: {dollarkurs}")
print(f"Wechselgebühr: {wechselgebühr}")
print(f"Endbetrag in Euro: {endbetrag:.2f}")

wunschendbetrag = float(input("Wunschendbetrag: "))
anfangskapital = wunschendbetrag / (dollarkurs * (1 - wechselgebühr))
print(f"Anfangskapital in Euro: {anfangskapital:.2f}")

print(type(1))
print(type(1.1))
print(type("Hallo"))
print(type(True))

print("\n", type(1 + 1))
print(type(1.1 + 1))
print(type("Hallo" + str(1)))
print(type(True + 1))
a = 1
print(type(a))
print(type(1.1 + 1.1))
print(type("Hallo" + "Welt"))
print(type(True + True))
print(type(False + False))
print(type(False + True))
print(type(False))

celsius = float(input("Temperatur in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperatur in Fahrenheit: {fahrenheit:.2f}")  # 2 Nachkommastellen

zahl1 = int(input("Erste Zahl: "))
zahl2 = int(input("Zweite Zahl: "))
print(f"Ergebnis der Division: {zahl1 / zahl2}")
print(f"Ergebnis der ganzzahligen Division: {zahl1 // zahl2}")
print(f"Ergebnis des Rests: {zahl1 % zahl2}")

bevorratung = float(input("Gesamtbevorratung in Litern: "))
verbrauch = float(input("Verbrauch in Litern: "))
vorrätig = bevorratung - verbrauch
prozent = vorrätig / bevorratung * 100
print(f"Es sind noch {vorrätig} Liter Bier vorrätig, das entspricht {prozent:.2f}% der Gesamtbevorratung.")

zahl = int(input("Ganze Zahl: "))
print(f"Die letzte Ziffer der Zahl ist: {zahl % 10}")
print(str(zahl)[-1])

masse = float(input("Masse in kg: "))
laenge = float(input("Körperlänge in m: "))
bmi = masse / laenge ** 2  # ** = Potenz
print(f"Ihr BMI beträgt: {bmi:.2f}")  # 2 Nachkommastellen

kommazahl = float(input("Kommazahl: "))
vor_komma = int(kommazahl)
nach_komma = kommazahl - vor_komma
print(f"Vorkommastellen: {vor_komma}")
print(f"Nachkommastellen: {nach_komma:.5f}")  # 5 Nachkommastellen

anzahl_studierende = int(input("Anzahl der Studierenden: "))
gruppengroesse = int(input("Gruppengröße: "))
anzahl_gruppen = anzahl_studierende // gruppengroesse
rest = anzahl_studierende % gruppengroesse  # % = Modulo
if rest > 0:
    anzahl_gruppen += 1
    print(
        f"Es ergeben sich {anzahl_gruppen} Gruppen mit einer Gruppengröße von {gruppengroesse} Studierenden. In der letzten Gruppe sind aber nur {rest} Studierende.")
else:
    print(f"Es ergeben sich {anzahl_gruppen} Gruppen mit einer Gruppengröße von {gruppengroesse} Studierenden.")

str = "Hallo"
print(str[-1])  # letztes Zeichen

""" Das Programm soll die Blutalkoholkonzentration (in Promille) anhand der von Benutzer:innen eingegebenen Werte ermitteln. Es gilt: Blutalkoholkonzentration (in Promille) = Masse des aufgenommenen Alkohols (in g) / Masse der Person (in kg) * Reduktionsfaktor. Zudem gilt: Masse des Alkohols (in g) = 10 * Volumen des Getränks (in l) * Alkoholvolumenanteil (in %) * 0,8. Der Reduktionsfaktor beträgt 0,7 bei Männern und 0,6 bei Frauen. Schreibe ein Programm, das Benutzer:innen nach ihrem Geschlecht, ihrer Masse und der Masse des aufgenommenen Alkohols fragt und die Blutalkoholkonzentration berechnet. """

# Lösung

geschlecht = input("Bist du männlich oder weiblich? ")
masse = float(input("Wie viel wiegst du (in kg)? "))
volumen = float(input("Wie viel Liter Alkohol hast du getrunken? "))
alkoholvolumenanteil = float(input("Wie viel Prozent Alkohol war in dem Getränk? "))

masse_alkohol = 10 * volumen * alkoholvolumenanteil * 0.8
red_faktor = 0.7 if geschlecht == "männlich" else 0.6
alkoholkonzentration = masse_alkohol / masse * red_faktor

print(f"Deine Blutalkoholkonzentration beträgt {alkoholkonzentration:.2f} Promille.")

""" In einem Studiensystem wird die Leistung der Studierenden nach einer numerischen Punktzahl bewertet. Schreibe ein Programm, dass Benutzer:innen nach einer erreichten Punktzahl fragt und eine entsprechende Bewertung zurückgibt: 90 bis 100 Punkte: "Sehr gut"; 80 bis 89 Punkte: "Gut"; 70 bis 79 Punkte: "Befriedigend"; 60 bis 69 Punkte: "Ausreichend"; Unter 60 Punkte: "Nicht bestanden". """

# Lösung
punkte = int(input("Wie viele Punkte hast du erreicht? "))

if 90 <= punkte <= 100:
    print("Sehr gut")
elif 80 <= punkte <= 89:
    print("Gut")
elif 70 <= punkte <= 79:
    print("Befriedigend")
elif 60 <= punkte <= 69:
    print("Ausreichend")
elif punkte < 60:
    print("Nicht bestanden")
else:
    print("Ungültig")

""" Schreibe ein Programm, in welchem Benutzer:innen drei Integer-Zahlen eingeben können. Das Programm soll den Maximalwert anhand dieser drei Zahlen auswählen, indem ausschließlich die if- und else-Anweisungen sowie der Größer-Gleich-Operator (>=) verwendet wird. Verwende keine anderen in Python oder Modulen integrierten Funktionen, die dir automatisch die größte Zahl auswählen. Tipps: Wenn A größer ist als B und C, ist A das Maximum. Wenn B größer ist als A und C ist B das Maximum. Gilt nichts hiervon, wird wohl C das Maximum sein. """

# Lösung
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))
zahl3 = int(input("Gib die dritte Zahl ein: "))

if zahl1 >= zahl2 and zahl1 >= zahl3:
    print(f"Maximalwert: {zahl1}")
elif zahl2 >= zahl1 and zahl2 >= zahl3:
    print(f"Maximalwert: {zahl2}")
else:
    print(f"Maximalwert: {zahl3}")

""" Das Programm soll die Blutalkoholkonzentration (in Promille) anhand der von Benutzer:innen eingegebenen Werte ermitteln. Es gilt: Blutalkoholkonzentration (in Promille) = Masse des aufgenommenen Alkohols (in g) / Masse der Person (in kg) * Reduktionsfaktor. Zudem gilt: Masse des Alkohols (in g) = 10 * Volumen des Getränks (in l) * Alkoholvolumenanteil (in %) * 0,8. Der Reduktionsfaktor beträgt 0,7 bei Männern und 0,6 bei Frauen. Schreibe ein Programm, das Benutzer:innen nach ihrem Geschlecht, ihrer Masse und der Masse des aufgenommenen Alkohols fragt und die Blutalkoholkonzentration berechnet. """

# Lösung

geschlecht = input("Bist du männlich oder weiblich? ")
masse = float(input("Wie viel wiegst du (in kg)? "))
volumen = float(input("Wie viel Liter Alkohol hast du getrunken? "))
alkoholvolumenanteil = float(input("Wie viel Prozent Alkohol war in dem Getränk? "))

masse_alkohol = 10 * volumen * alkoholvolumenanteil * 0.8
red_faktor = 0.7 if geschlecht == "männlich" else 0.6
alkoholkonzentration = masse_alkohol / masse * red_faktor

print(f"Deine Blutalkoholkonzentration beträgt {alkoholkonzentration:.2f} Promille.")

# BMI-Rechner
masse = float(input("Masse in kg: "))
laenge = float(input("Körperlänge in m: "))
bmi = masse / laenge ** 2  # ** = Potenz
print(f"Ihr BMI beträgt: {bmi:.2}")

""" Erweitere den bestehenden BMI-Rechner aus der vorherigen Einheit um eine Funktionalität, welche abhängig des errechneten BMIs mitteilt, ob die Benutzer:innen unter-, normal- oder übergewichtig, adipös sind. """

if bmi < 18.5:
    print("Untergewichtig")
elif 18.5 <= bmi < 25:
    print("Normalgewichtig")
elif 25 <= bmi < 30:
    print("Übergewichtig")
else:
    print("Adipös")

""" Teste break und continue sowie die for- als auch in while Schleifen. Überlege dir sinnvolle, konkrete Anwendungsfälle für die Verwendung von continue und break. """

# Lösung

# break
# Beispiel: Finde die erste Primzahl in einer Liste
zahlen = [4, 6, 7, 9, 10, 11, 12]
for zahl in zahlen:
    for i in range(2, zahl):
        if zahl % i == 0:
            break
    else:
        print(f"Die erste Primzahl in der Liste ist {zahl}")
        break

# continue
# Beispiel: Drucke alle geraden Zahlen von 0 bis 9
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

""" Schreibe ein Programm, welches die Zahlen von 100 bis 0 in absteigender Reihenfolge ausgibt. Nachdem die Zahl 0 ausgegeben wurde, folgt eine anschließende Botschaft, z.B. "Happy Birthday!" oder "Happy New Year" - diese erfolgt nur einmalig! """
import time

for i in range(100, -1, -1):
    print(i)
    time.sleep(1)
    if i == 0:
        print("Happy Birthday")

""" Schreibe ein Programm, das testet, ob Eingaben der Benutzer:innen ein Palindrom darstellt und das Prüfungs-Ergebnis ausgeben. Setze das gaze auch als reinen Zahlen-Palindrom-Checker um, wobei die eingegeben ganzen Zahlen nicht als Strings verarbeitet werden dürfen"""

# Lösung
wort = input("Geben Sie ein Wort ein: ")

if wort == wort[::-1]:
    print("Palindrom")
else:
    print("Kein Palindrom")

""" Das Programm soll ein einfaches Schachbrett ausgeben. Dieses besteht aus 8x8 Feldern, wobei sich abwechselnd schwarze und weiße Felder befinden. Nutzen Sie eine for-Schleife zur Erzeugung eines Schachbretts, bei dem weiße Felder als "W" und schwarze Felder als "S" dargestellt werden. Für Profis: Setze in ähnlicher Art und Weiße zudem ein Programm um, bei denen alle Dominosteine des Legespiels Domino in einem "Doppel-6er Dominoset" ausgegeben werden. Jeder Stein soll exakt einmal ausgegeben werden. Die Darstellung der Steine ist z.B.: [1|6] [2|6] usw. """

# Lösung
# Schachbrett
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("W", end=" ")
        else:
            print("S", end=" ")
    print()

print("\n")

# Dominosteine
for i in range(7):
    for j in range(i, 7):
        print(f"[{i + 1}|{j + 1}]", end=" ")
    print()

# TODO Finde und markiere die vorhandenen Fehler im folgenden Code:
print("Willkommen zum Altersrechner")

# alter_eingabe = input(
#     "Bitte gib dein Alter ein: ")  # Fehler: Eingabe ist ein String, sollte in Integer umgewandelt werden, Syntaxfehler
# if alter_eingabe > 18  # Fehler: Vergleichsoperator fehlt, Syntaxfehler
#     print("Du bist volljährig.")
# else  # Fehler: Syntaxfehler, fehlender Doppelpunkt
#     print("Du bist minderjährig.")
# if alter_eingabe = 18:  # Fehler: Zuweisung statt Vergleichsoperator, Syntaxfehler
#     print("Du bist genau 18 Jahre alt.")

print("Das Programm endet hier.")  # Fehler: Kein Fehler, aber unnötiger Kommentar

""" Entwickle ein Programm, das alle Primzahlen zwischen 1 und einer von den Benutzer:innen eingegebene Zahl findet. Dabei soll das Programm eine Schleife nutzen, um zu überprüfen, ob eine Zahl durch eine andere Zahl ohne Rest teilbar ist - ist eine Zahl eine Primzahl, wird sie ausgegeben. Gleiche dein Ergebnis gerne mit einer Primzahl-Auflistung aus dem Internet ab. Beachte Sonderfälle und fehlerhafte Eingaben etc."""

# Lösung
zahl = int(input("Gib eine Zahl ein: "))
for i in range(2, zahl):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

""" Schreibe ein Programm, das eine Zahl zwischen 1 und 3999 in römische Ziffern umwandelt. Verwende Verzweigungen, um zu entscheiden, welche römischen Symbole je nach Wert genutzt werde (z.B. "I" für 1 oder "V" für 5, "X" für 10, "L" für 50, etc.). Recherchiere die Funktionsweise römischer Zahlen im Zweifel im Internet. Beachte Sonderfälle und fehlerhafte Eingaben etc."""

# Lösung
zahl = int(input("Gib eine Zahl zwischen 1 und 3999 ein: "))

if not 1 <= zahl <= 3999:
    print("Ungültige Eingabe")
else:
    rom_zahlen = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
                  900: "CM", 1000: "M"}
    rom_zahl = ""
    for i in sorted(rom_zahlen.keys(), reverse=True):
        while zahl >= i:
            rom_zahl += rom_zahlen[i]
            zahl -= i
    print(rom_zahl)

""" Anhand einer Eingabe der Benutzer:innen sollen die korrekten binomischen Formeln formuliert werden. Werden zwei Zahlen eingegeben, wird die korrekte binomische Formel ausformuliert und das Egebnis berechnet. Wird eine Zahl und ein Buchstabe eingegeben, so wird die binomische Formel ohne Berechnung eines Ergebnisses ausgegeben. Werden zwei Buchstaben eingegeben, so wird die Regel für die korrekte binomische Formel ausgegeben. Beachte Sonderfälle und fehlerhafte Eingaben etc.  """

# Lösung
eingabe1 = input("Gib eine Zahl oder einen Buchstaben ein: ")
eingabe2 = input("Gib eine Zahl oder einen Buchstaben ein: ")

if eingabe1.isdigit() and eingabe2.isdigit():
    a = int(eingabe1)
    b = int(eingabe2)
    print(f"({a} + {b})^2 = {a ** 2} + 2*{a}*{b} + {b ** 2}")

elif eingabe1.isdigit() and eingabe2.isalpha():
    a = int(eingabe1)
    b = eingabe2
    print(f"({a} + {b})^2")

elif eingabe1.isalpha() and eingabe2.isdigit():
    a = eingabe1
    b = int(eingabe2)
    print(f"({a} + {b})^2")

elif eingabe1.isalpha() and eingabe2.isalpha():
    a = eingabe1
    b = eingabe2
    print(f"({a} + {b})^2")

else:
    print("Ungültige Eingabe")

import random

""" Entwickle ein Spiel, bei dem Benutzer:innen zwischen Kopf oder Zahl wählen können. Anschließend simuliert das Programm einen Münzwurf und gibt aus, ob die Benutzerinnen gewonnen haben"""

# Lösung
wahl = input("Kopf oder Zahl? ")
muenze = random.choice(["Kopf", "Zahl"])

if wahl == muenze:
    print("Gewonnen")
else:
    print("Verloren")

""" Entwickle ein Würfel spiel, bei dem zwei Benutzer:innen ("Spieler 1" und "Spieler 2" - oder man kann die Namen zu Beginn selbst eingeben) nacheinander raten müssen, auf welche Seite ein sechsseitiger Würfel fällt. """

# Lösung
Spieler1 = input("Spieler 1, gib deinen Namen ein: ")
Spieler2 = input("Spieler 2, gib deinen Namen ein: ")

wuerfel = random.randint(1, 6)
print(f"{Spieler1}, rate die Zahl: ")

while True:
    rate = int(input())
    if rate == wuerfel:
        print(f"{Spieler1} hat gewonnen!")
        break
    else:
        print("Falsch, rate nochmal: ")

""" Lasse dir ein zufälliges, sicheres Passwort generieren. Tipp: Verwende hierfür neben dem "random"-Modul auch das "string"-Modul. Mit der Zeile zeichen = string.ascii_letters + string.digits speicherst du eine Auflistung aller Buchstaben und Zahlen im ASCII-System in der Variable zeichen ab. Mit random.choice(zeichen) lässt sich jeweils ein Zeichen zufallsbasiert aussuchen. """

# Lösung
import random
import string

zeichen = string.ascii_letters + string.digits
passwort = "".join(random.choice(zeichen) for i in range(10))
print(passwort)
