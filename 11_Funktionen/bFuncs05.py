# immutable Parameter und mutable Parameter
def f1(x):
    x = [x[0]*2, x[1]*2]
    print("in der Funktion: ", x)

x = [1,2]
f1(x)
print("im Programm: ", x)

def f2(x):
    x.append(3)
    print("in der Funktion: ", x)

x = [1,2]
f2(x)
print("im Programm: ", x)