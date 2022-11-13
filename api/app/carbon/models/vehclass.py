import ormar

from ..db import BaseMeta


class VehClass(ormar.Model):
    class Meta(BaseMeta):
        tablename = "vehclass"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    label: str = ormar.String(max_length=64)
    description: str = ormar.String(max_length=255)