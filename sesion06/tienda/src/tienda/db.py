from fastapi import Depends
from typing import Annotated
from sqlmodel import create_engine, Session, SQLModel


# DATABASE_URL = "postgresql://<user>:<password>@<ip>:<port>/<database>"
DATABASE_URL = "postgresql://erick:1234@localhost:5432/tienda"

engine = create_engine(
    DATABASE_URL
)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def crear_tablas():
    SQLModel.metadata.create_all(engine)