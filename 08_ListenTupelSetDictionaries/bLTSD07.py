import locale

lst = list('Hello, World')
hwsorted = sorted(lst)
print(hwsorted)

mysort = sorted(lst, key=str.upper, reverse=True)
print(mysort)

locale.setlocale(locale.LC_ALL, 'german')
print(sorted(['a','b', 'ö', 'ä', 'ü', 's'], key=locale.strxfrm))