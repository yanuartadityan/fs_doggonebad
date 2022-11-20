import ormar

from ..db import BaseMeta


class Group(ormar.Model):
    class Meta(BaseMeta):
        tablename = "group"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    group_name: str = ormar.String(max_length=128)
    is_max_reached: bool = ormar.Boolean(default=False)
