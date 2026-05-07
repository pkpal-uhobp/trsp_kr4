from faker import Faker
from httpx import ASGITransport, AsyncClient
import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.main import app, reset_store

fake = Faker()


@pytest.fixture(autouse=True)
def _reset_state():
    reset_store()


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as async_client:
        yield async_client


def _make_user_payload() -> dict:
    return {
        "username": fake.user_name(),
        "age": fake.pyint(min_value=0, max_value=120),
    }


@pytest.mark.asyncio
async def test_create_user_success(client: AsyncClient):
    payload = _make_user_payload()
    response = await client.post("/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == payload["username"]
    assert data["age"] == payload["age"]


@pytest.mark.asyncio
async def test_get_user_success(client: AsyncClient):
    payload = _make_user_payload()
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_id, **payload}


@pytest.mark.asyncio
async def test_get_user_not_found(client: AsyncClient):
    response = await client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


@pytest.mark.asyncio
async def test_delete_user_success(client: AsyncClient):
    payload = _make_user_payload()
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]

    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 204
    assert response.text == ""


@pytest.mark.asyncio
async def test_delete_user_twice(client: AsyncClient):
    payload = _make_user_payload()
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]

    first = await client.delete(f"/users/{user_id}")
    assert first.status_code == 204

    second = await client.delete(f"/users/{user_id}")
    assert second.status_code == 404
    assert second.json()["detail"] == "User not found"
