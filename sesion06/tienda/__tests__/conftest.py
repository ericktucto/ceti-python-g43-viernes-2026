from sqlmodel import SQLModel
from tienda.db import crear_tablas
from fastapi.testclient import TestClient
from tienda.db import get_session
import pytest
from sqlmodel import Session
from sqlmodel import create_engine
from tienda import app

TEST_DATABASE_URL = "postgresql://erick:1234@localhost:5432/tienda_test"

test_engine = create_engine(
    TEST_DATABASE_URL
)

@pytest.fixture
def session():
    with Session(test_engine) as session:
        yield session

@pytest.fixture
def client(session: Session):
    def get_test_session():
        yield session

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as client:
        yield client

    

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(test_engine)

    yield

    SQLModel.metadata.drop_all(test_engine)