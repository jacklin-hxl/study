from sqlalchemy import Column, String
from .base import Base
from flask_login import UserMixin

from .. import login_manager


class User(UserMixin, Base):

    __tablename__ = "user"

    password = Column(type_=String(50), nullable=False)
    nickname = Column(type_=String(20), nullable=False)
    email = Column(type_=String(20))


@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
