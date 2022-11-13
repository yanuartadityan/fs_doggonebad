import ormar
import uuid
import datetime as dt

from typing import Optional, Dict, Union
from ..db import BaseMeta
from .group import Group


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)
    username: str = ormar.String(max_length=128, unique=True, nullable=False)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=128, nullable=False)
    is_active: bool = ormar.Boolean(default=True)
    date_created: dt.datetime = ormar.DateTime()

    # relationship columns put here
    group_id: Optional[Union[Group, Dict]] = ormar.ForeignKey(Group)