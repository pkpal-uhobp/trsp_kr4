from fastapi.testclient import TestClient

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from app.main import app

client = TestClient(app)


def main() -> None:
    ok = client.get("/")
    print("/ ->", ok.status_code, ok.json())

    bad_div = client.get("/divide", params={"x": 1, "y": 0})
    print("/divide?x=1&y=0 ->", bad_div.status_code, bad_div.json())

    not_found = client.get("/products/999")
    print("/products/999 ->", not_found.status_code, not_found.json())


if __name__ == "__main__":
    main()
