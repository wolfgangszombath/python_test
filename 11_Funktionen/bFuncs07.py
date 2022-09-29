# Parametertyp überprüfen
def f(n):
    if isinstance(n, int):
        print(n, ' ist eine Integerzahl!')
        return 2 * n
    elif isinstance(n, float):
        print(n, ' ist eine Gleitkommazahl!')
        return 2 * n
    else:
        print(n, " ist kein gültiger Parameter")
        return -1


print(f(3))
print(f(3.1415926))
print(f('abc'))

# Type Annotations
def f2(n: int) -> int:
    return 2 * n

print(f2(3))
print(f2(3.1416))
print(f2('abc'))