import ormar
import uuid

from typing import Optional, Union, Dict
from ..db import BaseMeta
from .platform import Platform
from .stop import Stop
from .mode_type import ModeType


class Drive(ormar.Model):
    class Meta(BaseMeta):
        tablename = "drive"

    # columns
    id: int = ormar.Integer(primary_key=True)
    uuid: uuid.UUID = ormar.UUID(uuid_format='hex', unique=True)

    # relational
    start_stop: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop)
    end_stop: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop)
    start_platform: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform)
    end_platform: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform)
    next_platform: Optional[Union[Platform, Dict]] = [ormar.ForeignKey(Platform)]
    type: Optional[Union[ModeType, Dict]] = ormar.ForeignKey(ModeType)