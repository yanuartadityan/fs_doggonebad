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
    platform_from: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_name="platform_to")
    platform_to: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_names="platform_from")
    type: Optional[Union[ModeType, Dict]] = ormar.ForeignKey(ModeType)