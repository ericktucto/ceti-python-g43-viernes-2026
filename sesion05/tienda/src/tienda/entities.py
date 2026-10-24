import uuid
from dataclasses import dataclass

@dataclass
class Producto:
    id: uuid.UUID
    nombre: str
    precio: int
    stock: bool


@dataclass
class Usuario:
    id: uuid.UUID
    nombre: str
    email: str
    password: str
