import asyncio
import datetime 

from carbon.db import database
from carbon.model import Group
from carbon.model import User


async def create():
    # Create some records to work with through QuerySet.create method.
    # Note that queryset is exposed on each Model's class as objects

    # method 2
    await Group.objects.create(
        group_name="Family-Doggonebad",
        is_max_reached=False
    )

    await Group.objects.create(
        group_name="Family-Catto",
        is_max_reached=False
    )

    await Group.objects.create(
        group_name="SMA34 Commuting Group",
        is_max_reached=False
    )

    a_group = await Group.objects.create(
        group_name="SMA8_JakSel_Team"
    )

    labrador = await User.objects.create(
        username="labrador",
        email="labrador@doggonebad.xyz",
        password="iambaddog",
        date_created=datetime.datetime.now()
    )

    await labrador.groups.add(a_group)
    await labrador.groups.add("SMA34 Commuting Group")

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