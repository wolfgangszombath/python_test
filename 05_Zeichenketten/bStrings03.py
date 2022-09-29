s = 'abcdefghijklmnopqrstuvwxyz'
#Ermitteln der Länge der Zeichenkette
lenOfS = len(s)
print("Die Zeichenkette ist " + str(lenOfS) + " Zeichen lang")
'''# Die einzelnen Buchstaben der Zeichenkette
for ch in s:
    print(ch)
print(30*'#')
for i in range(lenOfS-1,-1,-1):
    print(s[i])
print(30*'#')
'''
# Ein x-beliebiges Zeichen entnehmen - ACHTUNG Index startet bei Null
print(s[2])
# Eine bestimmte Anzahl an Zeichen [start:ende]
print(s[3:7])
# Zeichen bis zu einem bestimmten Punkt
print(s[:3])
# ab einem bestimmten Punkt
print(s[3:])
# das letzte Zeichen
print(s[-1])
# die 5 letzten Zeichen
print(s[-5:])
# bis zum 5 letzten Zeichen
print(s[:-5])
# Nur jedes zweite Zeichen
print(s[::2])
print(s[3:14:2])
# Umkehren der Zeichenkette
print(s[::-1])
# Vorsicht bei Bereichen
print(s[0:10])
print(30*"#")
print(s[0:10:-1])
print(30*"#")
print(s[11:0:-1])



