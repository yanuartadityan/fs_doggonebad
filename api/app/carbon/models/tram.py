from sqlalchemy import Boolean, Column, Integer, String, DateTime
from ..db import Base


class Tram(Base):
    __tablename__ = "tram"

    id = Column(Integer, primary_key=True, index=True)
    registration_id = Column(String, unique=True, index=True)
    production_date = Column(DateTime)
    next_service_date = Column(DateTime)
    overhaul_date = Column(DateTime)

    # potential relationship columns put here
    status = Column(Integer)
