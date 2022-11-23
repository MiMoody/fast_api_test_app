import datetime
import sqlalchemy
from .base import Base



# jobs = sqlalchemy.Table(
#     'jobs', 
#     meta_data,
#     sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True, autoincrement = True, unique = True),
#     sqlalchemy.Column('title', sqlalchemy.String),
#     sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False),
#     sqlalchemy.Column('description', sqlalchemy.String),
#     sqlalchemy.Column('is_active', sqlalchemy.Boolean),
#     sqlalchemy.Column('is_active', sqlalchemy.Boolean),
#     sqlalchemy.Column('salary_from', sqlalchemy.Integer),
#     sqlalchemy.Column('salary_to', sqlalchemy.Integer),
#     sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
#     sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow()),
# )

class Job(Base):
    
    __tablename__ = 'jobs'
    
    id = sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True, autoincrement = True, unique = True)
    title = sqlalchemy.Column('title', sqlalchemy.String)
    user_id = sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)
    description = sqlalchemy.Column('description', sqlalchemy.String)
    is_active = sqlalchemy.Column('is_active', sqlalchemy.Boolean)
    salary_from = sqlalchemy.Column('salary_from', sqlalchemy.Integer)
    salary_to = sqlalchemy.Column('salary_to', sqlalchemy.Integer)
    created_at = sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow())
    updated_at = sqlalchemy.Column('updated_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow())