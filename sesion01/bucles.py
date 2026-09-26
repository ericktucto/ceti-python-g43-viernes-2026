contador = 1

while contador <= 30:
    if contador % 2 == 0:
        print("Tu contador es par")
        contador += 1
        continue
    if contador == 17:
        break
    print("Tu contador es:", contador)
    #contador = contador + 1
    contador += 1

print("Fin del bucle")

print("BUCLE FOR")


for numero in range(1, 31):
    if numero % 2 == 0:
        print("Tu numero es par")
        continue
    if numero == 17:
        break
    print("Tu numero es:", numero)
