from dotenv import load_dotenv

load_dotenv()

import socketio
from sqlmodel import SQLModel, Session
from fastapi import FastAPI
from chat.routes import auth
from chat.db import engine
from chat.jwt import decode
from chat.repositories.usuario import UsuarioRepository


# servidor websockets
sio = socketio.AsyncServer(async_mode="asgi")

# servidor http
api = FastAPI()
api.frontend("/", directory="public")

# Auth Router
api.include_router(router=auth.router)

SQLModel.metadata.create_all(engine)

app = socketio.ASGIApp(sio, api)

@sio.event
async def connect(sid: str , environ, auth):
    token = (auth or {}).get("token")

    if not token:
        raise ConnectionRefusedError("token es requerido")

    claims = decode(token)
    if claims is None:
        raise ConnectionRefusedError("token invalido")

    usuario_id = claims.claims.get("data").get("usuario_id")

    with Session(engine) as session:
        repository = UsuarioRepository(session)

        usuario = repository.obtener_usuario_por_id(usuario_id)

        if not usuario:
            raise ConnectionRefusedError("usuario no existe")

        await sio.save_session(sid, {
            "usuario_id": usuario_id,
            "username": usuario.nombre
        })

    print("-" * 15, "conectado", sid, "usuario_id:", usuario_id)


@sio.on('join')
async def unirse(sid: str, datos: dict):
    session = await sio.get_session(sid)
    room = datos['room']
    username = session['username']

    await sio.save_session(sid, {
        "room": room,
        "username": username,
        "usuario_id": session['usuario_id']
    })

    await sio.enter_room(sid, room)
    await sio.emit('new-user', data={
        "id": sid,
        "username": username,
    }, room=room)

@sio.on('message')
async def mensaje(sid: str, datos: dict):
    sesion = await sio.get_session(sid)
    room = sesion["room"]
    username = sesion["username"]

    await sio.emit('message', data={
        "id": sid,
        "room": room,
        "username": username,
        "text": datos['text']
    }, room=room, skip_sid=sid)

@sio.on('typing')
async def tipiando(sid: str, datos: dict):
    sesion = await sio.get_session(sid)
    await sio.emit('typing', data={
        "id": sid,
        "name": sesion['username'],
        "typing": datos['typing'],
    }, room=sesion['room'], skip_sid=sid)

def main() -> None:
    print("Hello from chat!")
