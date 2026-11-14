from pydantic import BaseModel

class ProductoCreado(BaseModel):
    id: int
    nombre: str
    precio: int
    stock: bool
