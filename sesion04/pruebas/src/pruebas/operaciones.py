from pruebas.producto import Producto
def sumar(numero1: int, numero2: int) -> int:
    if type(numero1) != int or type(numero2) != int:
        raise ValueError("No esta pasando un numero (int)")
    return numero1 + numero2

def dividir(dividendo: float, divisor: float) -> float:
    return dividendo / divisor

def total(productos: list[Producto]) -> int:
    return sum([p.precio for p in productos])