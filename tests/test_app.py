import pytest
from src.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_start_route_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_start_route_content(client):
    response = client.get("/")
    assert b"Stop the world!" in response.data


def test_start_route_content_type(client):
    response = client.get("/")
    assert response.content_type == "text/html; charset=utf-8"


def test_invalid_route_returns_404(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_start_route_method_not_allowed(client):
    response = client.post("/")
    assert response.status_code == 405


if __name__ == "__main__":
    pytest.main()
