import ormar

from typing import Optional, Union, Dict
from ..db import BaseMeta
from .stop_type import StopType


class Stop(ormar.Model):
    class Meta(BaseMeta):
        __tablename__ = "stop"

    id: int = ormar.Integer(primary_key=True)
    initial: str = ormar.String(max_length=64)
    name: str = ormar.String(max_length=64)
    gps_lat: float = ormar.Float()
    gps_lon: float = ormar.Float()
    is_edge: bool = ormar.Boolean(default=False)
    is_atm: bool = ormar.Boolean(default=False)

    # relationship columns put here
    type: Optional[Union[StopType, Dict]] = ormar.ForeignKey(StopType)
