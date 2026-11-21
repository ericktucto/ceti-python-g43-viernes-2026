from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from chat.db import SessionDep
from chat.jwt import encode
from chat.repositories.usuario import UsuarioRepository
from chat.schemas.input.auth import LoginUsuario, RegistroUsuario
from chat.hashing import pwd


router = APIRouter(prefix='/api/auth', tags=['Autenticacion'])

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

