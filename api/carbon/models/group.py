import ormar

from ..db import BaseMeta


class Group(ormar.Model):
    class Meta(BaseMeta):
        tablename = "group"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    member_id: int = ormar.Integer()
    is_max_reached: bool = ormar.Boolean(default=False)

