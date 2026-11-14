from tienda.jwt import encode
from tienda.hashing import pwd
from tienda.schemas.inputs.auth import LoginUsuario
from tienda.repositories.usuario import UsuarioRepository
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from tienda.db import SessionDep
from tienda.schemas.inputs.auth import RegistroUsuario
from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/auth', tags=['autenticacion'])

@router.post('/registro')
def registro(datos_usuario: RegistroUsuario, session: SessionDep):
    repository = UsuarioRepository(session)
    usuario = repository.crear_usuario(datos_usuario)

    if usuario is None:
        raise HTTPException(status_code=422, detail="El usuario no se puede registrar")

    return JSONResponse(
        content={
            "id": usuario.id,
            "email": usuario.email,
            "nombre": usuario.nombre
        }
    )

@router.post("/login")
def login(datos_usuario: LoginUsuario, session: SessionDep):
    repository = UsuarioRepository(session)
    usuario = repository.obtener_usuario_por_correo(datos_usuario.email)

    if usuario is None:
        raise HTTPException(status_code=422, detail="El usuario no encontrado")

    checked = pwd.verify(datos_usuario.password, usuario.password)

    if checked is False:
        raise HTTPException(status_code=422, detail="Credenciales invalidas")

    token = encode({
        "usuario_id": usuario.id
    })

    return {
        "token": token,
    }