import asyncio
import datetime

from asyncpg.exceptions import UniqueViolationError
from carbon.db import database
from carbon.model import Group
from carbon.model import User


async def test():
    duracell, created = await User.objects.get_or_create(
        username="dura", email="duracell@gmail.com", password="aaa"
    )

    await duracell.groups.add(await Group.objects.create(group_name="alkaline"))


async def add_relation():
    # Create some records to work with through QuerySet.create method.
    # Note that queryset is exposed on each Model's class as objects

    await User.objects.create(
        username="labrador", email="labrador@doggo.com", password="doggo"
    )

    labrador = await User.objects.get(username="labrador")
    new_group = await Group.objects.get(id=13)
    await labrador.groups.add(new_group)

    chihuahua = await User.objects.get(username="chihuahua")
    await labrador.groups.add(await Group.objects.get(id=5))
    await labrador.groups.add(await Group.objects.get(id=12))
    await labrador.groups.add(await Group.objects.get(id=7))

    # to read more about inserting data into the database
    # visit: https://collerek.github.io/ormar/queries/create/


async def with_connect(function):
    # note that for any other backend than sqlite you actually need to
    # connect to the database to perform db operations
    async with database:
        await function()


for func in [test, add_relation]:
    print(f"executing {func.__name__}")
    asyncio.run(with_connect(func))
