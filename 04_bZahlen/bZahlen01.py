import operator
import sys

x = 2 ** 100
print(x)
print(type(x))
print(isinstance(x, int))

print(sys.maxsize)
print(2/3, 6/3)
print(2//3, 6//3)
print(2%3, 6%3)

hexX = 0xa0
print("Dezimal: " + str(hexX))
x = 160
print(hex(x))
hexX = hex(x)
print("Hexadezimal: " + str(hexX))
x = hexX


