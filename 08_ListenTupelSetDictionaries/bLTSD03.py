# Listen und Zeichenketten
hwlst = list('Hello, World!')
print(hwlst)
for c in hwlst:
    print(c)
print(30*"*")
# Zusammenfügen zu einer neuen Zeichenkette
hwlst_new = '#'.join(hwlst)
print("Original\n" + str(hwlst))
print("Nach #.join.\n" +str(hwlst_new))