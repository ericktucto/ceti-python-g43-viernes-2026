from pydantic import ConfigDict
from pydantic import BaseModel

class NuevoProducto(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "nombre": "Teclado inalambrico",
                    "precio": 30000,
                    "stock": True
                },
                {
                    "nombre": "WebCam",
                    "precio": 8000,
                    "stock": False
                }
            ]
        }
    )
    nombre: str
    precio: int
    stock: bool


class ActualizarProducto(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "examples": [
                {
                    "nombre": "Teclado inalambrico",
                    "precio": 30000,
                    "stock": True
                },
                {
                    "nombre": "WebCam",
                    "precio": 8000,
                    "stock": False
                }
            ]
        }
    )
    nombre: str
    precio: int
    stock: bool