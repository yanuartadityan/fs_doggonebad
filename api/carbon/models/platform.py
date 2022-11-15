import ormar

from typing import Optional, Union, Dict
from ..db import BaseMeta
from .stop import Stop
from .platform_type import PlatformType


class Platform(ormar.Model):
    class Meta(BaseMeta):
        tablename = "platform"

    # columns
    id: int = ormar.Integer(primary_key=True)
    initial: str = ormar.String(max_length=64, nullable=False)
    is_disabled_friendly: bool = ormar.Boolean(default=False)
    is_canopy: bool = ormar.Boolean(default=False)

    # relation
    stop_id: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop)
    type: Optional[Union[PlatformType, Dict]] = ormar.ForeignKey(PlatformType)