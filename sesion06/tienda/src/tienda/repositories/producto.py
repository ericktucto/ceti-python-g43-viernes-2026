from tienda.schemas.inputs.producto import ActualizarProducto
from tienda.schemas.inputs.producto import NuevoProducto
from tienda.db import SessionDep
from sqlmodel import select
from tienda.models.producto import Producto

class ProductoRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def todos_los_productos(self):
        return self.session.exec(
            select(Producto)
        ).all()

    def guardar_producto(self, datos: NuevoProducto) -> Producto:
        producto = Producto(
            nombre=datos.nombre,
            precio=datos.precio,
            stock=datos.stock
        )

        self.session.add(producto)
        self.session.commit()

        return producto

    def obtener_producto(self, id: int) -> Producto | None:
        return self.session.get(Producto, id)

    def actualizar_producto(self, id: int, datos: ActualizarProducto) -> Producto | None:
        producto_db = self.obtener_producto(id)

        if producto_db is None:
            return None

        producto_db.nombre = datos.nombre
        producto_db.precio = datos.precio
        producto_db.stock = datos.stock

        self.session.commit()

        return producto_db

    def eliminar_producto(self, id: int) -> Producto | None:
        producto_db = self.obtener_producto(id)

        if producto_db is None:
            return None

        self.session.delete(producto_db)
        self.session.commit()

        return producto_db