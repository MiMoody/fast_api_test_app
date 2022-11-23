import datetime
import json
from typing import List, Optional
from sqlalchemy import select, insert, update
from models.user import User, UserIn
from db.users import User as db_user
from .base import BaseDbRepository, BaseFileRepository
from core.security import hash_password, verify_password

class BaseUserRepository:
    
    async def get_all(self, limit :int = 100, skip :int = 0) -> List[User]:
       raise NotImplementedError
    
    async def get_by_id(self, id : int) -> Optional[User]:
        raise NotImplementedError
    
    async def get_by_email(self, email :str) -> User:
        raise NotImplementedError
    
    async def create(self, user_in :UserIn) -> User:
        raise NotImplementedError
    
    async def update(self, id :int, user_in :UserIn) -> User:
        raise NotImplementedError
    
    
class UserDbRepository(BaseUserRepository, BaseDbRepository):
    
    async def get_all(self, limit :int = 100, skip :int = 0) -> List[User]:
        query = select(db_user).limit(limit).offset(skip)
        return await self.database.fetch_all(query)
    
    async def get_by_id(self, id : int) -> Optional[User]:
        query = select(db_user).where(db_user.id == id).first()
        user  = await self.database.fetch_one(query)
        return user if User.parse_obj(user) else None
    
    async def get_by_email(self, email :str) -> User:
        query = select(db_user).where(db_user.id == email).first()
        user  = await self.database.fetch_one(query)
        return user if User.parse_obj(user) else None
    
    async def create(self, user_in :UserIn) -> User:
        user = User(
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
            is_company=user_in.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        values = {**user.dict()}
        values.pop('id', None)
        query = insert(db_user).values(**values)
        user.id = await self.database.execute(query)
        return user
    
    async def update(self, id :int, user_in :UserIn) -> User:
        user = User(
            id = id,
            name=user_in.name,
            email=user_in.email,
            hashed_password=hash_password(user_in.password),
            is_company=user_in.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow()
        )
        values = {**user.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        query = update(db_user).where(db_user.id==id).values(**values)
        await self.database.execute(query)
        return user
    
class UserFileRepository(BaseUserRepository, BaseFileRepository):
    
    pass
    