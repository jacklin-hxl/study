from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import TextClause

from app.models.base import Base


class Wish(Base):
    __tablename__ = "wish"

    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(20), nullable=False)
    launched = Column(type_=Boolean, server_default='0')
