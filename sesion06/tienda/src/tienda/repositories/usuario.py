from sqlmodel import select
from tienda.schemas.inputs.auth import RegistroUsuario
from tienda.db import SessionDep
from tienda.hashing import pwd
from tienda.models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    def crear_usuario(self, datos: RegistroUsuario) -> Usuario | None:
        usuario_correo = self.obtener_usuario_por_correo(datos.email)

        if usuario_correo is not None:
            return None

        hashed_password: str = pwd.hash(datos.password)

        nuevo_usuario = Usuario(
            nombre=datos.nombre,
            email=datos.email,
            password=hashed_password, # 123456
        )

        self.session.add(nuevo_usuario)
        self.session.commit()

        return nuevo_usuario

    def obtener_usuario_por_correo(self, email: str) -> Usuario | None:
        return self.session.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()