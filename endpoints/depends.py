from repositories.users import UserDbRepository
from db.base import database

def get_user_repository() -> UserDbRepository:
    return UserDbRepository(database)