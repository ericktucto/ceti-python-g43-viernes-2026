import uuid
from tienda.schemas.inputs.producto import ActualizarProducto, NuevoProducto
from tienda.schemas.outputs.producto import ProductoCreado
from tienda.entities import Producto
from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/api/v1/productos', tags=['productos'])

lista_productos: list[Producto] = []

@router.get('/')
def obtener_productos(q: str = ''):
    if q:
        respuesta: list[Producto] = []
        for p in lista_productos:
            if q in p.nombre:
                respuesta.append(p)
        return respuesta
    return lista_productos

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProductoCreado)
def crear_producto(datos: NuevoProducto):
    producto = Producto(
        id=uuid.uuid4(),
        nombre=datos.nombre,
        precio=datos.precio,
        stock=datos.stock
    )
    lista_productos.append(producto)

    return ProductoCreado(
        id=producto.id,
        nombre=producto.nombre,
        precio=producto.precio,
        stock=producto.stock
    )


@router.get('/{producto_id}')
def info_producto(producto_id: str):
    for p in lista_productos:
        if str(p.id) == producto_id:
            return p

    raise HTTPException(status_code=404, detail="Producto no encontrado")


@router.put('/{producto_id}')
def actualizar_producto(producto_id: str, datos: ActualizarProducto):
    producto: Producto | None = None
    for p in lista_productos:
        if str(p.id) == producto_id:
            producto = p
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    producto.nombre = datos.nombre
    producto.precio = datos.precio
    producto.stock = datos.stock

    return producto


@router.delete('/{producto_id}')
def eliminar_producto(producto_id: str):
    producto: int = -1
    for index, p in enumerate(lista_productos):
        if str(p.id) == producto_id:
            producto = index
    if producto == -1:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    lista_productos.pop(producto)

    return {"mensaje": "Producto eliminado"}
