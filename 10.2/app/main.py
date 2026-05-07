from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas import User, ValidationErrorResponse

app = FastAPI(title="User Validation API")


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    print(f"Validation error on {request.url.path}")
    payload = ValidationErrorResponse(
        code=422,
        message="Validation failed",
        errors=exc.errors(),
    )
    return JSONResponse(status_code=422, content=payload.model_dump())


@app.post("/users", responses={422: {"model": ValidationErrorResponse}})
def create_user(user: User):
    return {"status": "created", "user": user.model_dump()}

