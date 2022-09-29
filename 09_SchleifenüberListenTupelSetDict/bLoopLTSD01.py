# Wiederholung
for i in range(11):
    print(i, end="->")
print()
for i in range(30, 41, 2):
    print(i, end="-->")
print()
for i in range(100, 0, -10):
    print(i, end = '##')
print()
for i in range(0,10):
    x = i/10.0
    print(x, end = " ")
print()
# Schleifen über Zeichenketten
myString = "Hallo Welt - Hello World"
for c in myString:
    print(c, end = " * ")
print()
# Schleife über eine Liste
myList = ['Python', 'macht', 'viel', 'Spaß']
for el in myList:
    print(el)

# Schleife über numerierte Liste
myList = ['Python', 'Java', 'SQL', 'C#']
count = 1
for el in myList:
    print(count, el)
    count +=1
#Mit enumarte
for cnt, itm in enumerate(myList):
    print(cnt+1, itm)

