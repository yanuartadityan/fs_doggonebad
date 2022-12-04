from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from carbon.db import metadata, get_db_url
from carbon.model import *


url = get_db_url()
engine = create_engine(url, echo=True)

print(f'connecting to db:{url}')

metadata.drop_all(bind=engine)
metadata.create_all(bind=engine)
