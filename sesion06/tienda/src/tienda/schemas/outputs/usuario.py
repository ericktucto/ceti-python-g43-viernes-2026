import uuid
from pydantic import BaseModel

class UsuarioBasico(BaseModel):
    id: uuid.UUID
    nombre: str
    email: str