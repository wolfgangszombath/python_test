# Mit einem Generator
def fibgen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
# Fibonacci bis 1000
gen = fibgen(10)
fib = next(gen)

while fib < 1000:
    print(fib, sep=', ', end=' ')
    fib = next(gen)

#Die Lösung dafür
# while fib < 1000:
#     print(fib, sep=', ', end=' ')
#     fib = next(gen, None)
#     if fib == None:
#         print('Generaor erschöpft')
#         break