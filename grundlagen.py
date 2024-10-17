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
