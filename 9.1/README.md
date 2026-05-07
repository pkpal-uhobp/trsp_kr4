# Задание 9.1 — FastAPI + Alembic

Минимальный пример FastAPI-приложения с SQLAlchemy и Alembic для миграций.

## Шаги

1) Установить зависимости

```powershell
python -m pip install -r requirements.txt
```

2) Применить начальную миграцию

```powershell
alembic upgrade 0001_create_products
```

3) Добавить 2 записи (до второй миграции)

```powershell
python scripts\seed_products_initial.py
```

4) Применить миграцию с `description`

```powershell
alembic upgrade head
```

5) Запустить приложение (опционально)

```powershell
uvicorn app.main:app --reload
```

## Проверка схемы

В SQLite-файле `app.db` таблица `products` должна иметь поля: `id`, `title`, `price`, `count`, `description`.

## Примечания

- Если нужно сменить БД, задайте `DATABASE_URL` и обновите `alembic.ini`.
- Миграции лежат в `alembic/versions`.

