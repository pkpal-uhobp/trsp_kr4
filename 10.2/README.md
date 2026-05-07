# Задание 10.2 — FastAPI валидация и пользовательская обработка ошибок

Минимальный пример FastAPI-приложения с Pydantic-валидацией входных данных и обработчиком ошибок проверки.

## Шаги

1) Установить зависимости

```powershell
python -m pip install -r requirements.txt
```

2) Прогнать smoke-тест

```powershell
python scripts\smoke_test.py
```

3) Запустить приложение (опционально)

```powershell
uvicorn app.main:app --reload
```

## Эндпоинт

- `POST /users` принимает JSON с данными пользователя.

Пример валидного тела:

```json
{
  "username": "alice",
  "age": 25,
  "email": "alice@example.com",
  "password": "secret123",
  "phone": "+123456"
}
```

## Формат ошибки

При ошибке валидации ответ унифицирован:

```json
{
  "code": 422,
  "message": "Validation failed",
  "errors": [
    {
      "type": "value_error",
      "loc": ["body", "age"],
      "msg": "Input should be greater than 18",
      "input": 17
    }
  ]
}
```

