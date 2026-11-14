from sqlmodel import Field
from sqlmodel import SQLModel

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=False)
    precio: int = Field(index=False)
    stock: bool = Field(default=True)