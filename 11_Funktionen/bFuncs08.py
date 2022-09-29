# Rekursive Funktionen
def faculty(n):
    if n <=1:
        return 1
    else:
        return n * faculty(n-1)

for i in range(2,21):
    print('%2d mit der Fakultät %20d' %(i, faculty(i)))