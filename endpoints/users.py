from typing import List
from fastapi import APIRouter, Depends
from repositories.users import UserDbRepository, UserFileRepository
from models.user import User, UserIn
from .depends import get_user_repository


router = APIRouter()

# @router.get("/get", response_model = List[User], response_model_exclude={"hashed_password",})
# async def get(
#     users :UserFileRepository = Depends(lambda : UserFileRepository("./test.json")),
#     ):
#     return users.get()

@router.get("/get_users", response_model = List[User], response_model_exclude={"hashed_password",})
async def get_users(
    users :UserDbRepository = Depends(get_user_repository),
    limit :int = 100, 
    skip :int = 100
    ):
    return await users.get_all(limit=limit, skip=skip)

@router.post("/create_user", response_model = User, response_model_exclude={"hashed_password",})
async def create_user(
    user :UserIn,
    users :UserDbRepository = Depends(get_user_repository),
    ):
    return await users.create(user)

@router.patch("/update_user", response_model = User, response_model_include={"hashed_password",})
async def create_user(
    id :int,
    user :UserIn,
    users :UserDbRepository = Depends(get_user_repository),
    ):
    return await users.update(id, user) 