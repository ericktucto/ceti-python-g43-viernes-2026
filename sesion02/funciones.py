def hola():
    print("Hola que tal?")

def saludar(nombre, inicio = 'Hola'):
    return f"{inicio}, Soy {nombre}"

hola()
#edad = input("Dame tu edad: ")
mensaje = saludar("Erick", 'Buenos dias')

print(mensaje)

x = 5

def suma():
    y = 10
    return y + x

print(suma())
# print(y)

print("-" * 25, "Type hints")

nombre = "erick"
nombre = 123456

def area(
    base: int,
    altura: int
) -> int:
    return base * altura

print(area(5, 6))
print(area(5.8, 6))
print(area("hola ", 6))