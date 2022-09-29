lst = list(range(10,101,10))
print(lst)
# Anhängen eines Elementes
lst.extend([110])
# Anhängen mehrere Elemente
lst2 = list(range(100, 0, -10))
for i in lst2:
    lst.extend([i])
print(lst)
# Anhängen einer anderen Liste
lst.extend([list(range(120,141,5))])
print(lst)
# Einfügen eines Elementes
lst.insert(5, 55)
print(lst)
lst3 = list(range(51,60))
pos = 5
for i in lst3:
    lst.insert(pos, i)
    pos += 1
print(lst)
#Löschen eines Elementes nach Position
lst.pop(14)
print(lst)
lst.pop(-1)
print(lst)
# Löschen der letzten 3 Positionen
del lst[-3:]
print(lst)
# Entfernt einen bestimmte Zahl an Ihrem ersten Auftreten
lst.remove(100)
print(lst)
