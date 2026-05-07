from pathlib import Path

from sqlalchemy import Column, Integer, MetaData, Numeric, String, Table, create_engine
from sqlalchemy.orm import Session

BASE_DIR = Path(__file__).resolve().parents[1]
DB_URL = f"sqlite:///{(BASE_DIR / 'app.db').as_posix()}"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(200), nullable=False),
    Column("price", Numeric(10, 2), nullable=False),
    Column("count", Integer, nullable=False),
)


def main() -> None:
    with Session(engine) as session:
        session.execute(
            products.insert(),
            [
                {"title": "Keyboard", "price": 49.90, "count": 10},
                {"title": "Mouse", "price": 19.90, "count": 25},
            ],
        )
        session.commit()


if __name__ == "__main__":
    main()

