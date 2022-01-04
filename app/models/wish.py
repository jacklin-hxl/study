from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Wish(Base):
    __tablename__ = "wish"

    user = relationship("User")
    uid = Column(type_=Integer, ForeignKey="user.id")
    isbn = Column(type_=String(20), nullable=False, ForeignKey="book.isbn")
