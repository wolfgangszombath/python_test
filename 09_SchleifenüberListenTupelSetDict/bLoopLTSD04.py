for _ in range(10):
    print('bla', end = "/")

# mit Comprehension
print(['bla' for _ in range (10)])

# mit Generator
print(''.join('bla' for _ in range (10)))