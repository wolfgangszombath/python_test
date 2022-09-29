# normale Funktion
def fiblst(n):
    a, b = 0 , 1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result

print(fiblst(10))

# Mit einem Generator
def fibgen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

print(fibgen(10))
print(list(fibgen(10)))