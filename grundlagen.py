# # dollarkurs = float(input("Bitte geben Sie den Dollarkurs ein: "))
# # Kapital_in_euro = round(float(input("Bitte geben Sie das Kapital in Euro ein: ")), 2)
# # wechselgebühr = float(input("Bitte geben Sie die Wechselgebühr ein: "))
# # endbetrag = Kapital_in_euro * dollarkurs * (1 - wechselgebühr)
# #
# # print("\nAnfangskapital in Euro: ", Kapital_in_euro)
# # print("Dollarkurs:", dollarkurs)
# # print("Wechselgebühr:", wechselgebühr)
# # print(f"Endbetrag in Euro: {endbetrag:.2f}")
# #
# # # # wunschendbetrag eingeben und anfangskapital nicht kennen
# # # wunschendbetrag = float(input("Bitte geben Sie den Wunschendbetrag ein: "))
# # # anfangskapital = wunschendbetrag / (dollarkurs * (1 - wechselgebühr))
# # # print(f"Anfangskapital in Euro: {anfangskapital:.2f}")
# #
# # # print(type(1))
# # # print(type(1.1))
# # # print(type("Hallo"))
# # # print(type(True))
# # #
# # # #teste binäre operationen auf die typen
# # # print("\n", type(1 + 1))
# # # print(type(1.1 + 1))  # 1 wird als 1.0 interpretiert
# # # #print(type("Hallo" + 1)) # can only concatenate str (not "int") to str
# # # print(type(True + 1))  # funktioniert, weil True als 1 interpretiert wird
# # # # print(type(a)) # a nicht definiert
# # # print(type(1.1 + 1.1))
# # # print(type("Hallo" + "Welt"))
# # # print(type(True + True))  # True wird als 1 interpretiert
# # # print(type(False + False))  # False wird als 0 interpretiert
# # # print(type(False + True))  # False wird als 0 interpretiert
# # # print(type(False))
# #
# # """
# # float und int verrechnen wird zu float
# # str und int verrechnen geht nicht
# # str und str verrechnen geht
# # bool und int verrechnen geht
# # bool und bool verrechnen geht
# # float schneidet zahlen ab
# # """
#
# #celsius in fahrenheit
# celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
# fahrenheit = celsius * 9/5 + 32
# print(f"Die Temperatur in Fahrenheit beträgt: {fahrenheit:.2f}")
#
# #Analog zum im Beispiel betrachteten "Addierer" soll der "Divider" zwei Zahlen miteinander dividieren und Benutzer:innen geben zwei Zahlen ein, die als ganze Zahlen(int) gespeichert und weiterverarbeitet werden sollen. Anschließend werden Berechnungen anhand von drei Berechnungsweisen durchgeführt: zahl1/zahl2; zahl1//2, zahl1%zahl2.
# zahl1 = int(input("Bitte geben Sie die erste Zahl ein: "))
# zahl2 = int(input("Bitte geben Sie die zweite Zahl ein: "))
# ergebnis1 = zahl1 / zahl2
# ergebnis2 = zahl1 // zahl2
# ergebnis3 = zahl1 % zahl2
# print(f"Ergebnis der Division: {ergebnis1}")
# print(f"Ergebnis der ganzzahligen Division: {ergebnis2}")
# print(f"Ergebnis des Rests: {ergebnis3}")
#
# #Schreibe ein "Bierstands-Mess-Programm" für den Canstatter Wasen: Wirte und Wirtinnen sollen eingeben können, wie viel Bier sie insgesamt bevorraten haben und wie viel Liter Bier sie insgesamt bevorratet haben und wie viel Bier bereits verbraucht, sowie eine prozentuale Angabe, wie viel Bier noch vorrätig ist.
# bevorratung = float(input("Bitte geben Sie die Gesamtbevorratung in Litern ein: "))
# verbrauch = float(input("Bitte geben Sie den Verbrauch in Litern ein: "))
# vorraetig = bevorratung - verbrauch
# prozent = vorraetig / bevorratung * 100
# print(f"Es sind noch {vorraetig} Liter Bier vorrätig, das entspricht {prozent:.2f}% der Gesamtbevorratung.")
#
#
# #Schreibe ein Programm, welches Benutzer:innen nach einer ganzen Zahl fragt, und die letzte Ziffer dieser Zahl ausgibt. Löse die Aufgabe sowohl durch String-Formatierung als auch durch dir bekannte Rechenoperationen.
# zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))
# letzte_ziffer = zahl % 10
# print(f"Die letzte Ziffer der Zahl ist: {letzte_ziffer}")
#
# #Schreibe ein Programm, welches den BMI der Benutzer:innen berechnet. Es gilt BMI = Masse / Körperlänge^2
# masse = float(input("Bitte geben Sie Ihre Masse in kg ein: "))
# laenge = float(input("Bitte geben Sie Ihre Körperlänge in m ein: "))
# bmi = masse / laenge ** 2
# print(f"Ihr BMI beträgt: {bmi:.2f}")
#
# #Schreibe ein Programm, welches Benutzer:innen auffordert, eine Kommazahl einzugeben. Die eingebene Zahl wird anschließend in Vor- und Nachkommabestandteile zerlegt und wieder ausgegeben. Die Anzahl der Nachkommastellen wird auf fünf Stellen begrenzt.
# kommazahl = float(input("Bitte geben Sie eine Kommazahl ein: "))
# vor_komma = int(kommazahl)
# nach_komma = kommazahl - vor_komma
# print(f"Vorkommastellen: {vor_komma}")
# print(f"Nachkommastellen: {nach_komma:.5f}")
#
# #Recherchiere nochmals im Internet allgemein zu den skalaren Dateitypen in Python und den Möglichkeiten, die man bei deren Verarbeitung hat - insbesondere die Verarbeitungsmöglichkeiten von Strings werden dir später hilfreich sein. Geben Sie das aus.
# #Skalare Datentypen in Python sind: int, float, str, bool, complex
# #int: Ganzzahlen, Verwendung: Zahlen, die keine Nachkommastellen haben, z.B. Anzahl von Dingen, Alter, etc.
# #float: Gleitkommazahlen, Verwendung: Zahlen, die Nachkommastellen haben, z.B. Geldbeträge, Temperatur, Gewicht, Größe, etc.
# #str: Zeichenketten, Verwendung: Text, z.B. Namen, Adressen, etc.
# #bool: Wahrheitswerte (True, False), Verwendung: Ja/Nein, Wahr/Falsch, etc.
# # #complex: komplexe Zahlen (a + bi), Verwendung: mathematische Berechnungen, z.B. in der Elektrotechnik, Quantenmechanik, etc.

# Anzahl studierende eingeben, dann gruppengröße eingeben, dann Anzahl gruppen berechnen mit möglichst gleicher gruppengröße
anzahl_studierende = int(input("Bitte geben Sie die Anzahl der Studierenden ein: "))
gruppengroesse = int(input("Bitte geben Sie die Gruppengröße ein: "))
anzahl_gruppen = anzahl_studierende // gruppengroesse
rest = anzahl_studierende % gruppengroesse
if rest > 0:
    anzahl_gruppen += 1
print(
    f"Es ergeben sich {anzahl_gruppen} Gruppen mit einer Gruppengröße von {gruppengroesse} Studierenden. In der letzten Gruppe sind aber nur {rest} Studierende.")

str = "Hallo"
print(str[-1])
