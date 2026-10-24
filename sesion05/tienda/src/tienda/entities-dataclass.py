from pydantic import BaseModel
import uuid
from dataclasses import dataclass

@dataclass
class Producto:
    id: str
    nombre: str
    precio: int
    stock: bool

p1 = Producto(
    # id="1234",
    id=uuid.uuid4(),
    nombre="mouse",
    precio=4000,
    stock=True
)

class ProductoCreado(BaseModel):
    id: str
    nombre: str
    precio: int
    stock: bool

print(type(p1.id))
ProductoCreado(
    id=str(p1.id),
    nombre=p1.nombre,
    precio=p1.precio,
    stock=p1.stock
)