"""model.py"""
import datetime as dt
import uuid
from typing import Optional, List, Union, Dict
import ormar
from .db import BaseMeta


class StopType(ormar.Model):
    """StopType"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "stop_type"

    # table columns
    id: int = ormar.Integer(primary_key=True, autoincrement=False)
    label: str = ormar.String(max_length=64)
    description: str = ormar.String(max_length=255)


class PlatformType(ormar.Model):
    """PlatformType"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "platform_type"

    # table columns
    id: int = ormar.Integer(primary_key=True, autoincrement=False)
    label: str = ormar.String(max_length=64)
    description: str = ormar.String(max_length=255)


class ModeType(ormar.Model):
    """ModeType"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "mode_type"

    # table columns
    id: int = ormar.Integer(primary_key=True, autoincrement=False)
    label: str = ormar.String(max_length=64)
    description: str = ormar.String(max_length=255)


class VehType(ormar.Model):
    """VehType"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "vehtype"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    label: str = ormar.String(max_length=64)
    description: str = ormar.String(max_length=255)


class Group(ormar.Model):
    """Group"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "group"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)
    group_name: str = ormar.String(max_length=128, nullable=False)
    is_max_reached: bool = ormar.Boolean(default=False)
    

class User(ormar.Model):
    """User"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "user"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)
    username: str = ormar.String(max_length=128, unique=True, nullable=False)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=128, nullable=True)
    is_active: bool = ormar.Boolean(default=True)
    date_created: dt.datetime = ormar.DateTime()

    # relationship columns put here
    groups: Optional[List[Group]] = ormar.ManyToMany(Group)


class Owner(ormar.Model):
    """Owner"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "owner"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex', unique=True)
    company_name: str = ormar.String(max_length=128, nullable=False)
    company_reg: str = ormar.String(max_length=128, nullable=False)
    contact_number: str = ormar.String(max_length=128, nullable=False)
    contact_email: str = ormar.String(max_length=128, nullable=False)

    
class Stop(ormar.Model):
    """Stop"""
    class Meta(BaseMeta):
        """Metaclass"""
        __tablename__ = "stop"

    id: int = ormar.Integer(primary_key=True)
    initial: str = ormar.String(max_length=64)
    name: str = ormar.String(max_length=64)
    gps_lat: float = ormar.Float()
    gps_lon: float = ormar.Float()
    is_edge: bool = ormar.Boolean(default=False)
    is_atm: bool = ormar.Boolean(default=False)

    # relationship columns put here
    type: Optional[Union[StopType, Dict]] = ormar.ForeignKey(StopType)    


class Platform(ormar.Model):
    """Platform"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "platform"

    # columns
    id: int = ormar.Integer(primary_key=True)
    initial: str = ormar.String(max_length=64, nullable=False)
    is_disabled_friendly: bool = ormar.Boolean(default=False)
    is_canopy: bool = ormar.Boolean(default=False)

    # relation
    stop_id: Optional[Union[Stop, Dict]] = ormar.ForeignKey(Stop)
    type: Optional[Union[PlatformType, Dict]] = ormar.ForeignKey(PlatformType)


class Drive(ormar.Model):
    """Drive"""
    class Meta(BaseMeta):
        """Metaclass"""
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


class Stint(ormar.Model):
    """Stint"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "stint"

    # table columns
    id: int = ormar.Integer(primary_key=True)

    # relational
    platform_from: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_name="platform_to")
    platform_to: Optional[Union[Platform, Dict]] = ormar.ForeignKey(Platform, related_names="platform_from")
    type: Optional[Union[ModeType, Dict]] = ormar.ForeignKey(ModeType)


class Tram(ormar.Model):
    """Tram"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "tram"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex')
    reg_num: str = ormar.String(max_length=64, nullable=False)
    max_capacity: int = ormar.Integer()
    production_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())
    next_service_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())
    overhaul_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())

    # potential relationship columns put here
    owner_id: Optional[Union[Owner, Dict]] = ormar.ForeignKey(Owner)
    class_id: Optional[Union[VehType, Dict]] = ormar.ForeignKey(VehType)


class Bus(ormar.Model):
    """Bus"""
    class Meta(BaseMeta):
        """Metaclass"""
        tablename = "bus"

    # table columns
    id: int = ormar.Integer(primary_key=True)
    uid: uuid.UUID = ormar.UUID(default=uuid.uuid4, uuid_format='hex')
    reg_num: str = ormar.String(max_length=64, nullable=False)
    chassis_num: str = ormar.String(max_length=64, nullable=False)
    max_capacity: int = ormar.Integer()
    production_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())
    next_service_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())
    overhaul_date: dt.datetime = ormar.DateTime(default=dt.datetime.now())

    # potential relationship columns put here
    owner_id: Optional[Union[Owner, Dict]] = ormar.ForeignKey(Owner)
    class_id: Optional[Union[VehType, Dict]] = ormar.ForeignKey(VehType)
