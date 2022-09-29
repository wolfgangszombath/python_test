# Schreiben Sie eine Funktion, die dieQualität von Passwörtern nach
# einemeinfachen Punktesystem bewertet. Es gelten dabei die folgenden
# Regeln:
# – Passwortmit 7 oder weniger Zeichen: immer 0 Punkte
# – ab 8 Zeichen: 1 Punkt
# – enthält sowohl Groß- als auch Kleinbuchstaben: +1 Punkt
# – enthält mehr als sechs unterschiedliche Zeichen: +1 Punkt
# (Die Regel soll Passwörter wie »11111111« verhindern.)
# – enthält zumindest eine Ziffer: +1 Punkt
# – enthält zumindest ein Sonderzeichen: +1 Punkt
# Beispiele:
# – 'abc': 0 Punkte
# – 'abcdefghij': 2 Punkte
# – 'ab1122$$!!': 3 Punkte
# – 'abcd1234$!': 4 Punkte

def pwquality(s):
  if len(s)<8:
    return 0
  q = 1
  
  # >6 unterschiedliche Zeichen
  if len(set(s)) > 6: q+=1
  
  # Groß- und Kleinbuchstaben, Ziffern, Sonderzeichen
  hasdigit = False
  hasspecial = False
  hasupper = False
  haslower = False
  for c in s:
    if str.isupper(c): hasupper = True
    if str.islower(c): haslower = True
    if str.isdigit(c): hasdigit = True
    if not str.isalnum(c): hasspecial = True
  if hasupper and haslower: q+=1
  if hasdigit: q+=1
  if hasspecial: q+=1
  
  # Ergebnis zurückgeben
  return q

# Funktion für einige Zeichenketten testen        
tst = ['abc', 'abcdefghij', 'ab1122$$!!', 'abcd1234$!','Pa$$w0rd']
for p in tst:
  print('%s:\t%d Punkte' % (p, pwquality(p)))
