from sqlalchemy import Column, Integer, String, DateTime, Boolean
from ..db import Base


class Stop(Base):
    __tablename__ = "stop"

    initial = Column(String, primary_key=True, index=True)
    name = Column(String)
    platform = Column(String, index=True, nullable=False)
    gps_lat = Column(String)
    gps_lon = Column(String)
    is_disabled_friendly = Column(Boolean)

    # relationship columns put here