print("OPERADORES ARITMETICOS")
print("-" * 25)

print(18 + 4)

numero1 = 30
numero2 = 17

print(numero1 / numero2)
print(numero1 // numero2)
print(numero1 % numero2)

numero3 = 2

print(numero3 ** 5)

print("OPERADORES COMPARACION")
print("-" * 25)

print(numero1 == numero2)
print(numero1 == "30")
print(numero1 == 30)
print(numero1 >= 18)
print(numero2 >= 18)

numero2 = 18

print(numero2 >= 18)
print(numero2 > 18)
print("erick == erick ->", "erick" == "erick")

print("OPERADORES LOGICOS")
print("-" * 25)

print("True and True ->",   True and True)
print("True and False ->",  True and False)
print("False and True ->",  False and True)
print("False and False ->", False and False)

activo = True

# Software para Escuela
# Los alumnos mayores de 15 años y que tienen
# la ficha llenada pueden usar la piscina
edad_alumno = 16
ficha_llenada = True
edad_necesaria = edad_alumno >= 15

print(edad_necesaria and ficha_llenada)


print("True or True ->",   True or True)
print("True or False ->",  True or False)
print("False or True ->",  False or True)
print("False or False ->", False or False)

# email debe ser unico

correo_registrado = False
print(not correo_registrado)
