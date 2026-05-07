from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Product

app = FastAPI(title="Products API")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.id).all()
    return [
        {
            "id": product.id,
            "title": product.title,
            "price": float(product.price),
            "count": product.count,
            "description": product.description,
        }
        for product in products
    ]

