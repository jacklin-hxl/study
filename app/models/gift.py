from base import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class Gift(Base):
    """
    user - book  多对多关系
    一个用户可以赠送多个书籍， 一个数据可以被多个用户赠送
    Gift 记录user 和 book 业务模型关系
    """
    __tablename__ = "gift"

    user = relationship("User")
    uid = Column(type_=Integer, ForeignKey="user.id")
    isbn = Column(type_=String(20), nullable=False, ForeignKey="book.isbn")
    launched = Column(type_=Boolean, default=False)
