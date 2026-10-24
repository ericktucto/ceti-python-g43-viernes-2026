from pruebas.producto import Producto
from pruebas.operaciones import total, sumar, dividir
import pytest

def test_suma():
    assert sumar(7, 5) == 12

def test_suma_incorrecta():
    with pytest.raises(ValueError):
        sumar("12", 5)

@pytest.fixture
def productos():
    return [
        Producto("Teclado", 150),
        Producto("Mouse", 50)
    ]

def test_total(productos: list[Producto]):
    assert total(productos) == 200


def test_division_exacta():
    assert dividir(10, 5) == 2.0


def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
