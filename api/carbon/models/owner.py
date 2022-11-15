import ormar
import uuid

from ..db import BaseMeta


class Owner(ormar.Model):
    class Meta(BaseMeta):
        tablename = "owner"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)
    company_name: str = ormar.String(max_length=128, nullable=False)
    company_reg: str = ormar.String(max_length=128, nullable=False)
    contact_number: str = ormar.String(max_length=128, nullable=False)
    contact_email: str = ormar.String(max_length=128, nullable=False)