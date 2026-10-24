import uuid
from pydantic import BaseModel

class ProductoCreado(BaseModel):
    id: uuid.UUID
    nombre: str
    precio: int
    stock: bool
