from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from core.config import DATABASE_URL

Base = declarative_base() 

database = Database(DATABASE_URL)

meta_data = MetaData()

engine = create_engine(DATABASE_URL)

