from .base import Base, engine
from .users import User
from .jobs import Job

Base.metadata.create_all(engine)

Base.metadata.bind = engine