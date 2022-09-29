lst1 = [1, 2, 3, 9, 345 , 36, 33]
# lst2 enthält alle durch 3 teilbaren Elemente von l1
lst2 = list(filter(lambda x: x%3==0 , lst1))
print(lst2) # Ausgabe [3, 9, 345 , 36, 33]
# alle Elemente von l2 durch 3 dividieren
lst3 = list(map(lambda x: x//3 , lst2))
print(lst3) # Ausgabe [1, 3, 115 , 12, 11]

