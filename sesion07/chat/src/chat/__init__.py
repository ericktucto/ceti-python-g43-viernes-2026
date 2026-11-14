import socketio
from fastapi import FastAPI

sio = socketio.AsyncServer(async_mode="asgi")

api = FastAPI()
api.frontend("/", directory="public")

app = socketio.ASGIApp(sio, api)

@sio.event
async def connect(sid: str , environ, auth):
    print("-" * 15, "conectado", sid)


@sio.on('join')
async def unirse(sid: str, datos: dict):
    room = datos['room']
    username = datos['username']

    await sio.save_session(sid, {
        "room": room,
        "username": username,
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
