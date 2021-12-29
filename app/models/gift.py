from base import Base
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship
from user import User


class Gift(Base):
    """
    user - book  多对多关系
    一个用户可以赠送多个书籍， 一个数据可以被多个用户赠送
    Gift 记录user 和 book 业务模型关系
    """
    user = relationship("User")
    uid = Column(type_=Integer, ForeignKey="user.id")
