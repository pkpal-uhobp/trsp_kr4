from fastapi import FastAPI

from app.exceptions import CustomExceptionA, CustomExceptionB
from app.handlers import handle_custom_exception_a, handle_custom_exception_b
from app.schemas import ErrorResponse

app = FastAPI(title="Error Handling API")

app.add_exception_handler(CustomExceptionA, handle_custom_exception_a)
app.add_exception_handler(CustomExceptionB, handle_custom_exception_b)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/divide", responses={400: {"model": ErrorResponse}})
def divide(x: float, y: float):
    if y == 0:
        raise CustomExceptionA(message="Division by zero", details="Parameter 'y' must be non-zero")
    return {"result": x / y}


@app.get("/products/{product_id}", responses={404: {"model": ErrorResponse}})
def get_product(product_id: int):
    if product_id != 1:
        raise CustomExceptionB(message="Product not found", details=f"No product with id={product_id}")
    return {"id": 1, "title": "Sample", "price": 9.99}

