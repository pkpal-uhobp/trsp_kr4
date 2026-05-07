from pathlib import Path
import sys

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.main import app

client = TestClient(app)


def main() -> None:
    ok_payload = {
        "username": "alice",
        "age": 25,
        "email": "alice@example.com",
        "password": "secret123",
        "phone": "+123456",
    }
    ok = client.post("/users", json=ok_payload)
    print("/users ok ->", ok.status_code, ok.json())

    bad_payload = {
        "username": "bob",
        "age": 17,
        "email": "not-an-email",
        "password": "short",
    }
    bad = client.post("/users", json=bad_payload)
    print("/users bad ->", bad.status_code, bad.json())


if __name__ == "__main__":
    main()

