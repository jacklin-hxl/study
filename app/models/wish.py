from flask_login import current_user
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

    @classmethod
    def in_wishes(cls, isbn):
        flag = False
        if current_user.is_authenticated:
            if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                    launched=False).first():
                flag = True

        return flag

