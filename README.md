## Общие требования

- Все команды ниже рассчитаны на Windows PowerShell.
- Перед запуском перейдите в папку нужного задания.

## Задание 9.1 — FastAPI + Alembic

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\9.1"
python -m pip install -r requirements.txt
alembic upgrade 0001_create_products
python scripts\seed_products_initial.py
alembic upgrade head
```

Опционально запустить API:

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\9.1"
uvicorn app.main:app --reload
```

## Задание 10.1 — Пользовательская обработка ошибок

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\10.1"
python -m pip install -r requirements.txt
python scripts\smoke_test.py
```

Опционально запустить API:

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\10.1"
uvicorn app.main:app --reload
```

## Задание 10.2 — Валидация и обработка ошибок

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\10.2"
python -m pip install -r requirements.txt
python scripts\smoke_test.py
```

Опционально запустить API:

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\10.2"
uvicorn app.main:app --reload
```

## Задание 11.1 — Тесты pytest

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\11.1"
python -m pip install -r requirements.txt
pytest -q
```

Опционально запустить API:

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\11.1"
uvicorn app.main:app --reload
```

## Задание 11.2 — Асинхронные тесты

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\11.2"
python -m pip install -r requirements.txt
pytest -q
```

Опционально запустить API:

```powershell
Set-Location "C:\Users\User\PycharmProjects\trsp_kr4\11.2"
uvicorn app.main:app --reload
```
