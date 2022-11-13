import ormar

from typing import Optional, Union, Dict
from ..db import BaseMeta
from .mode_type import ModeType
from .platform import Platform


class Stint(ormar.Model):
    class Meta(BaseMeta):
        tablename = "stint"

    # table columns
    id: int = ormar.Integer(primary_key=True)

    # relational
    platform_from: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform)
    platform_to: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform)
    type: Optional[Union[ModeType, Dict]] = ormar.ForeignKey(ModeType)