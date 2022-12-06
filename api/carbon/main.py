# app/main.py
from fastapi import FastAPI
from carbon.db import database
from carbon.crud import user
from typing import List

# main App
app = FastAPI(
    title="CliniqueAPI"
)

# router
app.include_router(user.router)

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


@app.get("/")
async def get_root():
    return {
        'status': 'OK',
        'hello': 'world'
    }
