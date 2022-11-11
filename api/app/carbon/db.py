# app/db.py
import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from ..config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

Base = declarative_base()

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)