import asyncio

from carbon.db import database
from carbon.model import *


async def clean_constant():
    await VehType.objects.delete(each=True)
    await ModeType.objects.delete(each=True)
    await PlatformType.objects.delete(each=True)
    await StopType.objects.delete(each=True)

async def clean_tables():
    await User.objects.delete(each=True)
    await Group.objects.delete(each=True)
    await Owner.objects.delete(each=True)

    await Stop.objects.delete(each=True)
    await Platform.objects.delete(each=True)
    await Stint.objects.delete(each=True)

    await Bus.objects.delete(each=True)
    await Tram.objects.delete(each=True)
    await Drive.objects.delete(each=True)


async def with_connect(function):
    async with database:
        await function()

        
for func in [
    clean_constant,
    clean_tables
]:
    print(f"executing {func.__name__}")
    asyncio.run(with_connect(func))