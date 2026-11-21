from pydantic import BaseModel


class RegistroUsuario(BaseModel):
    nombre: str
    email: str
    password: str

class LoginUsuario(BaseModel):
    email: str
    password: str
