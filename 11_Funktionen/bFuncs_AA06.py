# Schreiben Sie eine rekursive Funktion, die den größten
# gemeinsamen Teiler (den ggT) von zwei Zahlen berechnet. Dabei
# handelt es sich um die größte Zahl, durch den beide Zahlen ohne Rest
# dividiert werden können. Ihre Funktion soll den euklidischen Algorithmus implementieren.

def ggt(a, b):
    if a < b: 
        a, b = b, a
    rest = a % b
    if rest == 0:
        # ggT gefunden
        return b
    else:
        # rekursiver Aufruf
        return ggt(b, rest)
        
n1 = int(input('Zahl 1: '))
n2 = int(input('Zahl 2: '))
print('Der ggT von %d und %d beträgt %d.' % \
      (n1, n2, ggt(n1, n2)))
