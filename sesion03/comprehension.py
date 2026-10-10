# List Comprehension
# [expresion for variable in iterable condicional]

# Set Comprehension
# {expresion for variable in iterable condicional}

# Dict Comprehension
# {clave: valor for variable in iterable condicional}

productos_dolares = {
    "pan": 3,
    "manquilla": 2,
    "mermelada": 4,
}

print("Precios en dolares", productos_dolares)
productos_soles = { nombre: dolar * 3.5 for nombre, dolar in productos_dolares.items() }
print("Precios en soles", productos_soles)


alumnos = {
    "Ana": 12,
    "Juan": 18,
    "Marcos": 11,
    "Debora": 8,
    "Pedro": 10
}

alumnos_aprobados = {
    nombre: nota
    for nombre, nota in alumnos.items()
    if nota > 10
}

print("Alumnos aprobados", alumnos_aprobados)
