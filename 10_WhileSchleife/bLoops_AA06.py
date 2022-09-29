'''
Formulieren Sie eine Schleife, um den Wertebereich zwischen unterer Grenze
und oberer Grenze in einer bestimmten Anzahl von Schritten zu durchlaufen. Das Programm soll alle Zahlen
ausgeben, beginnend mit der unteren Grenze und endend mit der oberen Grenze
'''

min = float(input("Geben Sie die untere Grenze ein (Kommazahl)\n"))
max = float(input("Geben Sie die obere Grenze ein (Kommazahl)\n"))
nmax = int(input("Geben Sie die Anzahl der Stufen ein! (Ganzzahl)\n"))
delta = (max - min) / (nmax - 1)

for i in range(0, nmax):
  x = min + delta * i
  print("%.2f" % x)
