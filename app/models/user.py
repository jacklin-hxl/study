from sqlalchemy import Column, String, Integer
from base import Base


class User(Base):

    password = Column(type_=String(20))
    username = Column(type_=String(20))
