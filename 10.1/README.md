# Задание 10.1 — FastAPI пользовательская обработка ошибок

Минимальный пример FastAPI-приложения с пользовательскими исключениями, обработчиками и моделью ответа об ошибке.

## Шаги

1) Установить зависимости

```powershell
python -m pip install -r requirements.txt
```

2) Запустить smoke-тест обработчиков

```powershell
python scripts\smoke_test.py
```

3) Запустить приложение (опционально)

```powershell
uvicorn app.main:app --reload
```

## Эндпоинты

- `GET /divide?x=1&y=0` -> `CustomExceptionA` (400)
- `GET /products/{product_id}` -> `CustomExceptionB` (404 при id != 1)

## Формат ошибки

Ответы об ошибках приводятся к единому виду:

```json
{
  "code": 400,
  "message": "Division by zero",
  "details": "Parameter 'y' must be non-zero"
}
```

