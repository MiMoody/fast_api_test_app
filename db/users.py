import datetime
import sqlalchemy
from .base import Base


# users = sqlalchemy.Table(
#     'users', 
#     meta_data,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True, autoincrement = True, unique = True),
#     sqlalchemy.Column('name', sqlalchemy.String),
#     sqlalchemy.Column('email', sqlalchemy.String, primary_key = True, unique = True),
#     sqlalchemy.Column('hashed_password', sqlalchemy.String),
#     sqlalchemy.Column('is_company', sqlalchemy.Boolean),
#     sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
#     sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
    
# )



class User(Base):
    
    __tablename__ = 'users'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True, autoincrement = True, unique = True)
    name = sqlalchemy.Column(sqlalchemy.String(250))
    email = sqlalchemy.Column(sqlalchemy.String(40), primary_key = True, unique = True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    is_company = sqlalchemy.Column(sqlalchemy.Boolean)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())