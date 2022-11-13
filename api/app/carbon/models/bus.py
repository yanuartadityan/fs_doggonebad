import ormar
import uuid
import datetime as dt

from typing import Optional, Dict, Union
from ..db import BaseMeta
from .owner import Owner
from .vehclass import VehClass

class Bus(ormar.Model):
    class Meta(BaseMeta):
        tablename = "bus"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uuid: uuid.UUID = ormar.UUID(uuid_format='hex')
    reg_num: str = ormar.String(max_length=64, nullable=False)
    chassis_num: str = ormar.String(max_length=64, nullable=False)
    max_capacity: int = ormar.Integer()
    production_date: dt.datetime = ormar.DateTime(dt.datetime.now())
    next_service_date: dt.datetime = ormar.DateTime(dt.datetime.now())
    overhaul_date: dt.datetime = ormar.DateTime(dt.datetime.now())

    # potential relationship columns put here
    owner_id: Optional[Union[Owner, Dict]] = ormar.ForeignKey(Owner)
    class_id: Optional[Union[VehClass, Dict]] = ormar.ForeignKey(VehClass)
