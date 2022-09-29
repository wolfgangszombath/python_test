'''
Berechnen Sie die Summe der Funktion 1/x^2
, wenn Sie für x alle Zahlen zwischen 2 und 1000 einsetzen.
Brechen Sie die Schleife ab, wenn die Schrittgröße unter 0,00001 liegt!
'''
import math

sum = 0
for i in range(2, 1000):
    step = 1 / math.pow(i,2)
    sum += step
    print("%d\tZwischensumme %.4f \tSchrittweite: %.8f"% (i, sum, step))
    if step < 0.00001: break
print("Gesamtsumme: %.6f" % sum)
