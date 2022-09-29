word1 = set(input("Geben Sie ein Wort ein\n").lower())
word2 = set(input("Geben Sie ein Wort ein\n").lower())
#Welche Elemente
resUnion = word1 | word2
print("Vereinigung: " + str(sorted(resUnion)))
resDiff = word1 - word2
print("Diffrerenz: " + str(sorted(resDiff)))
resIntersect = word1 & word2
print("gemeinsame ELemente: " + str(sorted(resIntersect)))
resXOR = word1 ^ word2
print("unterschiedliche Elemente: " + str(sorted(resXOR)))
