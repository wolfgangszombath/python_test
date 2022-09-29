# Funktion ohne Rückgabe
def output(x,y):
    print('Parameter 1: ', x)
    print('Parameter 2: ', y)
    print('Summe: ', summe(x,y))

# Funktion mit Rückgabe
def summe(x,y):
    return x + y

# Funktion ohne Parameter und ohne Rückgabe
def error():
    print('Keine Zahl!')

wert1 = input("Geben Sie eine ganze Zahl ein\n")
wert2 = input("Geben Sie eine noch ganze Zahl ein\n")

output(wert1,wert2) if (wert1.isdigit() and wert2.isdigit()) else error()