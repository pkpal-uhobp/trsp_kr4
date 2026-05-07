# Задание 11.2 — Асинхронные тесты FastAPI

Минимальное FastAPI-приложение и асинхронные тесты с pytest-asyncio, httpx.AsyncClient (ASGITransport) и Faker.

## Эндпоинты

- `POST /users` — создать пользователя
- `GET /users/{user_id}` — получить пользователя
- `DELETE /users/{user_id}` — удалить пользователя

## Установка

```powershell
python -m pip install -r requirements.txt
```

## Запуск тестов

```powershell
pytest -q
```

## Примечания

- В тестах используется `Faker` для генерации данных.
- Состояние in-memory хранилища очищается перед каждым тестом.
- Тесты работают без запуска сервера через `ASGITransport`.
