import copy

a=[1,2,3]
b = copy.copy(a)
a[0] = a[0]*4
print(a, b)