# app/main.py
from fastapi import FastAPI
from app.carbon.db import database
from app.carbon.models import user, stop, tram

app = FastAPI(
    title="CliniqueAPI"
)

@app.get("/")
async def read_root():
    return False

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()

    # create a dummy
    return False

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

