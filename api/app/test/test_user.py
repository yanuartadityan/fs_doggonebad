import asyncio
import datetime as dt
from app.carbon.models.user import User
from app.carbon.db import database


async def create():
    # Create some records to work with through QuerySet.create method.
    # Note that queryset is exposed on each Model's class as objects

    # method 1
    tolkien = await User.objects.create(
        username="doggo",
        email="doggo@doggonebad.xyz",
        password="12345",
        date_created=dt.datetime.now()
        )
   
    # method 2
    await User.objects.create(
        username="golden",
        email="golden@doggonebad.xyz",
        password="12345",
        date_created=dt.datetime.now()
        )

    # to read more about inserting data into the database
    # visit: https://collerek.github.io/ormar/queries/create/

async def with_connect(function):
    # note that for any other backend than sqlite you actually need to
    # connect to the database to perform db operations
    async with database:
        await function()

for func in [create]:
    print(f"executing {func.__name__}")
    asyncio.run(with_connect(func))