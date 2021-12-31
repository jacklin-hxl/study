from sqlalchemy import Column, String
from app.models.base import Base


class User(Base):

    __tablename__ = "user"

    password = Column(type_=String(50), nullable=False)
    nickname = Column(type_=String(20), nullable=False)
    email = Column(type_=String(20))
