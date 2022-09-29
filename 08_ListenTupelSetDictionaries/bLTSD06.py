#map!!!
import math
from functools import reduce

def quadrat(x):
    return math.pow(x,2)
lst = list(range(1,6))
print (lst)
iterator = map(quadrat, lst)
print(list(iterator))

lambdaList = list(map(lambda x: x*x, lst))
print(lambdaList)

print([x*x for x in lst])

def sum(x, y):
    return x+y

lst1 = [7,1,4]
lst2 = [10,11,12]
lst3 = lst1 + lst2
print(lst3)
lst3 = list(map(sum, lst1, lst2))
print(lst3)
#reduce Berechnet eine Funktion über eine Liste
lst = list(range(1,101))
print(reduce(lambda x,y: x+y, lst))

#filter
ergebnis = filter(lambda x: x%2==0, lst)
print(list(ergebnis))