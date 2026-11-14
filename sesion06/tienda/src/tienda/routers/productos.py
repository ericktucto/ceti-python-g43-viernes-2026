from typing import Annotated
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from tienda.jwt import verificar_token
from fastapi import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from tienda.repositories.producto import ProductoRepository
from tienda.schemas.inputs.producto import ActualizarProducto, NuevoProducto
from tienda.schemas.outputs.producto import ProductoCreado
from tienda.db import SessionDep
from tienda.models.producto import Producto as ProductoModel
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/api/v1/productos', tags=['productos'])

bearer = HTTPBearer()

@router.get('/')
def obtener_productos(session: SessionDep):
    repository = ProductoRepository(session)
    return repository.todos_los_productos()


@router.get('/{producto_id}')
def info_producto(session: SessionDep, producto_id: int):
    repository = ProductoRepository(session)
    producto = repository.obtener_producto(producto_id)

    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    return producto


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductoCreado)
def crear_producto(
    session: SessionDep,
    datos: NuevoProducto,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)]
):
    if not verificar_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="Acceso no autoriado")

    repository = ProductoRepository(session)
    producto = repository.guardar_producto(datos)

    return ProductoCreado(
        id=producto.id,
        nombre=producto.nombre,
        precio=producto.precio,
        stock=producto.stock
    )


@router.put('/{producto_id}')
def actualizar_producto(session: SessionDep, producto_id: int, datos: ActualizarProducto):
    repository = ProductoRepository(session)
    producto_db = repository.actualizar_producto(producto_id, datos)

    if producto_db is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {
        "id": producto_db.id,
        "nombre": producto_db.nombre,
        "precio": producto_db.precio,
        "stock": producto_db.stock
    }


@router.delete('/{producto_id}')
def eliminar_producto(session: SessionDep, producto_id: int):
    repository = ProductoRepository(session)
    producto_db = repository.eliminar_producto(producto_id)

    if producto_db is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {"mensaje": "Producto eliminado"}
