# Evaluar la nota de alumno

# 1) Pedir nota del alumno
nota = int(input("Ingresa tu nota "))

# 2) Dar mensaje de evaluacion
if nota <= 11:
    print("Desaprobaste")
    print("----------")


if 12 <= nota <= 14:
    print("Necesitas un examen de recuperacion")
print("No estoy dentro de la condicional")


print("-" * 10, "Metodo 2", "-" * 10)

if nota <= 11:
    print("Desaprobaste")
    print("----------")
elif nota <= 14:
    print("Necesitas un examen de recuperacion")
elif nota <= 19:
    print("Aprobaste")
elif nota == 20:
    print("Aprobaste con una nota sobresaliente")
else:
    print("La nota es incorrecta")

