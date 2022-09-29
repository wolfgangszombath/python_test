import random

lst = []
for i in range(20):
    lst.append(int(random.uniform(0,15)))
print(lst)
lstSimplify = set(lst)
print(lstSimplify)

