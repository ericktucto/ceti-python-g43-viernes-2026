from os import getenv
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine


DATABASE_URL: str = getenv('DATABASE_URL') or ''

engine = create_engine(
    DATABASE_URL
)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
