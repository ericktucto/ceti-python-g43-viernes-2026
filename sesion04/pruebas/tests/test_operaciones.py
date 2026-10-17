from pruebas.producto import Producto
from pruebas.operaciones import total
import pytest
from pruebas.operaciones import sumar

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