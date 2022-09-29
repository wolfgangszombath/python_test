# Die in Python vordefinierten Funktionen min und max ermitteln
# das kleinste bzw. größte Element einer Liste. Programmieren Sie die
# Funktion minmax, die die beiden entsprechenden Elemente als Tupel
# zurückgibt – natürlich, ohne auf min und max zurückzugreifen.
def minmax(lst):
    min = lst[0]
    max = lst[0]
    for itm in lst:
        if itm<min:
            min = itm
        if itm>max:
            max = itm
    return (min, max)
        
nmbs = [-13, 27, 59, -70, 44]
a, b = minmax(nmbs)
print('Minimum: %d   Maximum: %d' % (a, b))
# So wäre natürlich am einfachsten!
print('Minimum: ', min(nmbs), 'Maximum: ', max(nmbs))
