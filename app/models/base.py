import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as SQLAlchemy_, BaseQuery as BaseQuery_
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


class BaseQuery(BaseQuery_):

    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs["status"] = 1

        return super(BaseQuery, self).filter_by()


db = SQLAlchemy(query_class=BaseQuery)


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

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.datetime.fromtimestamp(self.create_time)
        else:
            return None
