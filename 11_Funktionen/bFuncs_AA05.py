# Schreiben Sie eine Funktion, die eine Zeichenkette nach allen
# Vorkommen einer anderen Zeichenkette durchsucht und die Startpositionen
# als Liste zurückgibt.

def findAll(s, pattern):
    matches = []
    pos = s.find(pattern)
    while pos != -1:
        matches += [pos]
        pos = s.find(pattern, pos+1)
    return matches
    
print(findAll('abcefgabcxyzabcd', 'abc'))
