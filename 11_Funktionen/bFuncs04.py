# def f1():
#     z += 3
#     print(z)


# def f1():
#     global z # Sollte aber eher vermieden werden!
#     z +=3
#     print(z)

# eine bessere Lösung
def f1(x):
    z = x + 3
    print(z)

z=3
f1(z)