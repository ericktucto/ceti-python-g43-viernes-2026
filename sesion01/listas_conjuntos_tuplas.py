frutas = ["manzana", "pera", "uva", "kiwi", "mango"]

for fruta in frutas:
    if fruta == "pera":
        print("Tengo una fruta pera")
        continue
    print("Tengo esta fruta", fruta)

print(frutas)
print(frutas[1])
print(frutas[-1])

frutas[1] = "coco"
print(frutas)

frutas.append("sandia")
print("sandia agregada", frutas)
frutas.insert(0, "durazno")
print("durazno agregada", frutas)

eliminado = frutas.pop(1)
print(frutas, eliminado)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros[::3])


numeros2 = (10, 20, 37, 40, 13)
print(numeros2[2])
# numeros2[2] = 75
print({1, 2, 2, 3, 3, 4, 5, 6, 6, 7})
print({"peru", "chile", "venezuela", "ecuador", "peru"})
