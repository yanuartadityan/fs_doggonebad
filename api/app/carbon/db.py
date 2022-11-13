# app/db.py
import databases
import ormar
import sqlalchemy

from ..config import settings

# define database to be used
database = databases.Database(settings.db_url)

# derived metadata from SQLAlchemy
metadata = sqlalchemy.MetaData()

# create basemodel
class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata