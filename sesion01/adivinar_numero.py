import random

aleatorio: int = random.randint(1, 100)
intentos = 1

print("== ADIVINA EL NÚMERO ==")
print("Pienso un número del 1 al 100.")

def get_opcion(mensaje):
    opcion = input(mensaje)
    try:
        return int(opcion)
    except ValueError:
        return None

while True:
    numero = get_opcion("Escoge un numero: ")
    if numero is None:
        print("No es valido el numero")
        continue
    if numero == aleatorio:
        break
    elif numero < aleatorio:
        print("Muy bajo")
    else:
        print("Muy alto")
    intentos +=1


print(f"!Correcto! en {intentos} intento(s)")