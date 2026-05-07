from fastapi.testclient import TestClient

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.main import app

client = TestClient(app)


def setup_function():
    client.post("/reset")


def test_register_user_success():
    response = client.post(
        "/users",
        json={"username": "alice", "email": "alice@example.com"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"


def test_register_user_invalid_email():
    response = client.post(
        "/users",
        json={"username": "alice", "email": "not-an-email"},
    )
    assert response.status_code == 422


def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_get_user_success():
    created = client.post(
        "/users",
        json={"username": "bob", "email": "bob@example.com"},
    ).json()
    response = client.get(f"/users/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_delete_user_success():
    created = client.post(
        "/users",
        json={"username": "carol", "email": "carol@example.com"},
    ).json()
    response = client.delete(f"/users/{created['id']}")
    assert response.status_code == 200
    assert response.json() == {"status": "deleted", "id": created["id"]}

    follow_up = client.get(f"/users/{created['id']}")
    assert follow_up.status_code == 404


def test_delete_user_not_found():
    response = client.delete("/users/123")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
