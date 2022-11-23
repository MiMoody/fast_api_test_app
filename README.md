###  Использование миграций ### 
- Установка alembic: pip install alembic
- Создать папку с настройками alembic: alembic init alembic
- В файле alembic.ini поменять только параметр подключения к бд: sqlalchemy.url, например, postgresql://user_name:pass@localhost:5432/name_db
- В файле ./alembic/env.py необходимо в параметр target_metadata установить metadata sqlalchemy, импортировав его из файла, например, 
    from db import base
    target_metadata = base.meta_data
- Для запуска миграции необходимо прописать: alembic revision --autogenerate -m "my commit"
- Для применения миграции  необходимо прописать:  alembic upgrade head