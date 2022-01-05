import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as SQLAlchemy_
from sqlalchemy import Column, Integer, SmallInteger


class SQLAlchemy(SQLAlchemy_):

    # 继承SQLAlchemy ，新增上下文管理器，用于事务提交和回滚
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    create_time = Column(Integer)
    id = Column(type_=Integer, autoincrement=True, primary_key=True)
    status = Column(SmallInteger, server_default='1')

    def __init__(self):
        self.create_time = int(datetime.datetime.now().timestamp())

    def set_attrs(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
