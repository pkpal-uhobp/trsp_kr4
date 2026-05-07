from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import CustomExceptionA, CustomExceptionB
from app.schemas import ErrorResponse


def handle_custom_exception_a(request: Request, exc: CustomExceptionA) -> JSONResponse:
    print(f"CustomExceptionA: {exc.message}")
    payload = ErrorResponse(code=exc.status_code, message=exc.message, details=exc.details)
    return JSONResponse(status_code=exc.status_code, content=payload.model_dump())


def handle_custom_exception_b(request: Request, exc: CustomExceptionB) -> JSONResponse:
    print(f"CustomExceptionB: {exc.message}")
    payload = ErrorResponse(code=exc.status_code, message=exc.message, details=exc.details)
    return JSONResponse(status_code=exc.status_code, content=payload.model_dump())

