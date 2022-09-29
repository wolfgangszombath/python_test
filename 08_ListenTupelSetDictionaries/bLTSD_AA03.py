vocals = ('a','e','i','o','u','ä','ö','ü')
text = input("Geben Sie einen Satz ein\n")
text = list(text)
print(text)
resVoc = [x for x in text if x not in vocals]
print(resVoc)
resCons = [c for c in text if c in vocals]
print(resCons)