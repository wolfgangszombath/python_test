#optionale Parameter
def myFunc(a,b, c=-1, d=8):
    print(a,b,c,d)

myFunc(6,7,8,9)
myFunc(6,7,9)
myFunc(6,7)
myFunc(a=6,b=7,d=15)
myFunc(6,7, c=67)

# beliebige Anzahl an Parametern
def myFunc2(*a):
    print(a)

myFunc2(1,2,3,4)
myFunc2(1,2,3)
# mit einer Liste
myList = [1,2,3,4,5,6]
myFunc2(myList)

#mit List Comprehension
myList = [1,2,3,4,5]
print(*[x*x for x in myList])

