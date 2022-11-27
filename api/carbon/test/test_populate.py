import asyncio
import names
import hashlib
import random
import datetime as dt
import uuid

from carbon.db import database
from carbon.model import User, Group, Owner
from carbon.model import Stop, Platform, Stint, ModeType, PlatformType, StopType
from carbon.model import Bus, Tram, VehClass, Drive


DUMMY_DOMAIN = [
    "yahoo.com",
    "google.com",
    "hotmail.com",
    "aio.com",
    "bing.com",
    "outlook.com",
    "microsoft.com"
]

DUMMY_COMPANY = [
    ["jaya lestari", "ID-5535-ABCD-EFGH", "031-456789-03", "co.id"],
    ["sumber kencono", "ID-P354-XXYY-MNBC", "031-352773-88", "com"],
    ["lrt jaksel", "JKT-7732-B7UJ-ABCD", "021-9985127-012", "gov.id"],
    ["burung biru", "JKT-1827-BLAS-KA9J", "021-6628361-028", "com"]
]

DUMMY_GROUP = [
    "Family",
    "DaBoyz",
    "JKTCommuters",
    "BSD-Bicycle-Club",
    "Kuningan Royal Elite",
    "Permata Commuter Club",
    "Senior Club"
]

async def clean_all():
    await User.objects.delete(each=True)
    await Group.objects.delete(each=True)
    await Owner.objects.delete(each=True)

    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)

    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)
    await Stop.objects.delete(each=True)


async def populate_users():

    # populate User
    for _ in range(20):
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        username = '.'.join([firstname, lastname]).lower()

        domain = random.choice(DUMMY_DOMAIN)
        email = '@'.join([username, domain])

        await User.objects.create(
            username=username,
            email=email,
            # simply hash the username to get dummy pass
            password=hashlib.md5(username.encode('utf-8')).hexdigest(),
            date_created=dt.datetime.now()
        )

    # populate Owner
    for company in DUMMY_COMPANY:
        contact = '.'.join([names.get_first_name(), names.get_last_name()]).lower()
        domain = company[0].replace(' ', '') + f'.{company[3]}'

        await Owner.objects.create(
            uid=uuid.uuid4(),
            company_name=company[0].upper(),
            company_reg=company[1],
            contact_number=company[2],
            contact_email='@'.join([contact, domain])
        )

    # populate Group
    for group in DUMMY_GROUP:
        await Group.objects.create(
            uid=uuid.uuid4(),
            group_name=group
        )


async def populate_stops():
    pass

async def populate_vehicles():
    pass

async def populate_constant():
    pass

async def with_connect(function):
    async with database:
        await function()

for func in [
    clean_all,
    populate_users
]:
    print(f"executing {func.__name__}...")
    asyncio.run(with_connect(func))