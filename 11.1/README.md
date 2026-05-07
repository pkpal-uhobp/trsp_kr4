# Задание 11.1 — FastAPI + pytest

Минимальный пример FastAPI-приложения с тремя эндпоинтами и модульными тестами на pytest.

## Эндпоинты

- `POST /users` — регистрация пользователя
- `GET /users/{user_id}` — получение пользователя
- `DELETE /users/{user_id}` — удаление пользователя

## Установка

```powershell
python -m pip install -r requirements.txt
```

## Запуск тестов

```powershell
pytest -q
```

## Примечания

- Хранилище — in-memory `dict`.
- Тесты используют `TestClient` и сбрасывают состояние через `POST /reset`.

