from sqlalchemy import Column, String, Integer
from .base import Base


class Book(Base):

    __tablename__ = "book"

    title = Column(type_=String(50), nullable=False)
    author = Column(type_=String(20), default="未知")
    binding = Column(type_=String(20))
    publisher = Column(type_=String(50))
    pages = Column(type_=Integer)
    pubdate = Column(type_=String(20))
    summary = Column(type_=String(1000))
    image = Column(type_=String(50))
    isbn = Column(type_=String(20), nullable=False, unique=True)
    price = Column(type_=String(20))

