from pruebas.operaciones import total
from pruebas.producto import get_productos
def main() -> None:
    productos = get_productos()
    total(productos)
