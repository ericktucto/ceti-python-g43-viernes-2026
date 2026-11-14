import uuid
from dataclasses import dataclass


@dataclass
class Usuario:
    id: uuid.UUID
    nombre: str
    email: str
    password: str
