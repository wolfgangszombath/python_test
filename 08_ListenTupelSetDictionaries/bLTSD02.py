# Zweidimensionale Listen
lst = [[1,2],[3,4]]
print(lst[0])

#List die einzelenen Elemente der Unterlisten aus
for i in range (len(lst)):
    for j in lst[i]:
        print(j)

# range Funktion in Listen
lst = list(range(10,101,10))
print(lst)
lst = list(range(100,0,-10))
print(lst)