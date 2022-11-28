import asyncio
import names
import hashlib
import random
import datetime as dt
import uuid

from carbon.db import database
from carbon.model import User, Group, Owner
from carbon.model import Stop, Platform, Stint, ModeType, PlatformType, StopType
from carbon.model import Bus, Tram, VehType, Drive


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

DUMMY_STOP_TYPE = [
    [1, "Bus"],
    [2, "KRL"],
    [3, "Reserved"],
    [4, "MRT"],
    [5, "Reserved"],
    [6, "Reserved"],
    [7, "Reserved"],
    [8, "LRT"],
    [9, "Reserved"],
    [10, "Reserved"],
    [11, "Reserved"],
    [12, "Reserved"],
    [13, "Reserved"],
    [14, "Reserved"],
    [15, "Reserved"],
    [16, "Reserved"]

]

DUMMY_MODE_TYPE = [
    [1, "Bus"],
    [2, "KRL"],
    [4, "MRT"],
    [8, "KA"],
]

DUMMY_PLATFORM_TYPE = [
    [1, "Roadside"],
    [2, "Underground"],
    [4, "Multi-Stories"],
    [8, "Reserved"],
    [16, "Reserved"]
]

DUMMY_STOP = [
    ["LBS", "Lebak Bulus", 4],
    ["FWT", "Fatmawati", 2],
    ["BLA", "Blok A", 2],
    ["BLM", "Blok M", 3],
    ["SYN", "Senayan", 4],
    ["KNG", "Kuningan", 2],
    ["SDM", "Sudirman", 4],
    ["THA", "Thamrin", 2],
    ["MNS", "Monas", 4],
    ["POI", "Pondok Indah", 2],
    ["CDG", "Ciledug", 2],
    ["BIN", "Bintaro", 2],
    ["JUR", "Jurang Mangu", 2],
    ["SDR","Sudimara", 2],
    ["SRP", "Serpong", 2],
    ["TAB", "Tanah Abang", 2] 
]

async def clean_all():
    await User.objects.delete(each=True)
    await Group.objects.delete(each=True)
    await Owner.objects.delete(each=True)

    await Stop.objects.delete(each=True)
    await Platform.objects.delete(each=True)
    await Stint.objects.delete(each=True)
    await ModeType.objects.delete(each=True)
    await PlatformType.objects.delete(each=True)
    await StopType.objects.delete(each=True)

    await Bus.objects.delete(each=True)
    await Tram.objects.delete(each=True)
    await VehType.objects.delete(each=True)
    await Drive.objects.delete(each=True)


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
    
    # populate Stop
    for stop in DUMMY_STOP:
        # current stop
        curr_stop = Stop(
            initial=stop[0],
            name=stop[1],
            gps_lat=random.uniform(-6.8, -5.4),
            gps_lon=random.uniform(104.0, 110.0)
        )

        # save the stop (update database)
        await curr_stop.save()

        # populate Platform
        for plat_idx in range(stop[2]):
            curr_platform = Platform(
                initial=f"{stop[0]}_{plat_idx}",
                is_disabled_friendly=random.choice([True, False]),
                is_canopy=random.choice([True, False]),
                stop_id=curr_stop
            )

            await curr_platform.save()


async def populate_vehicles():
    pass

async def populate_constant():
    
    # populate stop type
    for stype in DUMMY_STOP_TYPE:
        await StopType.objects.create(
            id=stype[0],
            label=stype[1],
            description="reserved..."
        )

    # populate mode type
    for mtype in DUMMY_MODE_TYPE:
        await ModeType.objects.create(
            id=mtype[0],
            label=mtype[1],
            description="reserved..."
        )

    # populate platform type
    for ptype in DUMMY_PLATFORM_TYPE:
        await PlatformType.objects.create(
            id=ptype[0],
            label=ptype[1],
            description="reserved..."
        )

    # populate vehicle class

async def with_connect(function):
    async with database:
        await function()

for func in [
    clean_all,
    populate_constant,
    populate_users,
    populate_stops,
]:
    print(f"executing {func.__name__}...")
    asyncio.run(with_connect(func))