from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float

producto1 = Producto(nombre="Teclado mecanico", precio=180)

print(producto1)

class Usuario:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Usuario(nombre='{self._nombre}')"

usuario1 = Usuario("Erick")

print(
    "-> Tu objecto usuario:",
    str(usuario1)
)