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
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)

    # relational
    start_stop: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop, related_name="end_stop")
    end_stop: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop, related_name="start_stop")
    start_platform: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_name="end_platform")
    end_platform: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_name="start_platform")
    next_platform: Optional[Union[Platform, Dict]] = [ormar.ForeignKey(Platform)]
    type: Optional[Union[ModeType, Dict]] = ormar.ForeignKey(ModeType)