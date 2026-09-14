from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_openapi_is_available():

    response = client.get("/openapi.json")

    assert response.status_code == 200


def test_swagger_docs_is_available():

    response = client.get("/docs")

    assert response.status_code == 200