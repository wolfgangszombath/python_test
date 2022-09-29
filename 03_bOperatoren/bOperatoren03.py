a = 'abc'
b = 'abc'

if a==b:
    print("Der Inhalt der Variablen a und b ist gleich!")
else:
    print("Der Inhalt der Variablen a und b ist nicht gleich!")

if a is b:
    print("a und b verweisen auf dasselbe Objekt")
else:
    print("a und b verweisen nicht auf dasselbe Objekt")


b=a

if a==b:
    print("Der Inhalt der Variablen a und b ist gleich!")
else:
    print("Der Inhalt der Variablen a und b ist nicht gleich!")

if a is b:
    print("a und b verweisen auf dasselbe Objekt")
else:
    print("a und b verweisen nicht auf dasselbe Objekt")