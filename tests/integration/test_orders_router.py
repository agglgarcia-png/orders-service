from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_openapi_contains_orders_routes():

    response = client.get("/openapi.json")

    assert response.status_code == 200

    paths = response.json()["paths"]

    assert "/orders" in paths
    assert "/orders/{order_id}" in paths
    assert "/orders/{order_id}/status" in paths


def test_orders_post_endpoint_exists():

    response = client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "post" in paths["/orders"]


def test_orders_get_endpoint_exists():

    response = client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "get" in paths["/orders/{order_id}"]


def test_orders_patch_endpoint_exists():

    response = client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "patch" in paths["/orders/{order_id}/status"]


def test_orders_delete_endpoint_exists():

    response = client.get("/openapi.json")

    paths = response.json()["paths"]

    assert "delete" in paths["/orders/{order_id}"]


def test_swagger_docs_available():

    response = client.get("/docs")

    assert response.status_code == 200


def test_openapi_available():

    response = client.get("/openapi.json")

    assert response.status_code == 200