from fastapi import FastAPI
import uvicorn
from db.base import database
from core.router import set_routers


app = FastAPI(title= "Name app")


@app.on_event("startup")
async def startup():
    set_routers(app)
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    

if __name__ == "__main__":
    uvicorn.run("main:app" ,port=8000, host="0.0.0.0", reload=True)