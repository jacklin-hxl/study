from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = Column(type_=Integer, autoincrement=True, primary_key=True)
    status = db.Column(SmallInteger, default=1)
