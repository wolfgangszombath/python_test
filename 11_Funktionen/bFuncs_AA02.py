# Schreiben Sie eine Funktion, die testet, ob eine Zeichenkette ein Palindrom
# ist. Tipp: Verwenden Sie die Funktion str.isalpha, umzu testen,
# ob ein Zeichen ein Buchstabe ist.
def palindrom(s):
    lst = list(s.lower())
    plainlst = filter(str.isalpha, lst)
    plain = ''.join(plainlst)
    return plain == plain[::-1]

# Funktion für einige Zeichenketten testen        
tst = ['Lagerregal',
       'Trug Tim eine so helle Hose nie mit Gurt?',
       'Die Liebe ist Sieger; stets rege ist sie bei Leid',
       'Blabla',
       'Python ist cool']
for p in tst:
  if palindrom(p):
    print("'", p, "' ist ein Palindrom.", sep='')
  else:
    print("'", p, "' ist kein Palindrom.", sep='')