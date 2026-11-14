from fastapi.testclient import TestClient

def test_obtener_productos(client: TestClient):
    response = client.get('/api/v1/productos')

    assert response.status_code == 200

