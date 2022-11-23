from fastapi import FastAPI
from endpoints import users


def set_routers(app :FastAPI):
    app.include_router(users.router, prefix = "/users", tags=['users'])
    
