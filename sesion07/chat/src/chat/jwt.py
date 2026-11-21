from joserfc.jwt import Token
from joserfc.errors import JoseError
from os import getenv
from joserfc import jwt, jwk
import time

JWT_SECRET = getenv('JWT_SECRET') or ''

key = jwk.import_key(JWT_SECRET, "oct")


def encode(data: dict) -> str:
    payload = {
        "exp": int(time.time()) + 3600,
        "data": data
    }


    return jwt.encode(
        {"alg": "HS256"},
        payload,
        key
    )

def decode(token: str) -> Token | None:
    try:
        return jwt.decode(token, key)
    except JoseError:
        return None

def verificar_token(token: str) -> bool:
    decoded = decode(token)
    return type(decoded) == Token

