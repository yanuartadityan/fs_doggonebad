# app/main.py
from fastapi import FastAPI
from carbon.db import database


app = FastAPI(
    title="CliniqueAPI"
)


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