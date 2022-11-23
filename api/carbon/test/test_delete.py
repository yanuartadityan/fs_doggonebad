import asyncio

from carbon.db import database
from carbon.models.group import Group
from carbon.models.user import User


async def clear_groups():
    await Group.objects.delete(each=True)

async def clear_users():
    await User.objects.delete(each=True)

async def with_connect(function):
    async with database:
        await function()

        
for func in [clear_groups, clear_users]:
    print(f"executing {func.__name__}")
    asyncio.run(with_connect(func))