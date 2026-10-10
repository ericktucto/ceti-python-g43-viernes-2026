

def generador():
    for i in range(1, 10_000_000):
        yield i

#print(generador())

for elemento in generador():
    print(elemento)