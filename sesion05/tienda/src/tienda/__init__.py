from tienda.schemas.outputs.usuario import UsuarioBasico
from tienda.entities import Usuario
from tienda.routers import productos
from fastapi import FastAPI
import uuid

app = FastAPI()

@app.get('/')
def hola():
    return { "mensaje": "Hola Erick" }

@app.get('/api/v1/usuarios')
def obtener_usuario():
    usuario = Usuario(
        id=uuid.uuid4(),
        nombre="Erick Tucto",
        email="erick@ericktucto.com",
        password="secreto"
    )
    return UsuarioBasico(
        id=usuario.id,
        nombre=usuario.nombre,
        email=usuario.email
    )

app.include_router(productos.router)
