from flask import current_app
from sqlalchemy.sql.elements import TextClause

from .base import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..spider.yushu_book import YuShuBook
from ..view_models.book import BookSingle


class Gift(Base):
    """
    user - book  多对多关系
    一个用户可以赠送多个书籍， 一个数据可以被多个用户赠送
    Gift 记录user 和 book 业务模型关系
    """
    __tablename__ = "gift"

    user = relationship("User")
    uid = Column(Integer, ForeignKey("user.id"))
    isbn = Column(String(20), nullable=False)
    launched = Column(type_=Boolean,  server_default='0')

    @classmethod
    def recent(cls):
        # fixme 时间排序存在问题
        recent_list = Gift.query.with_entities(
            cls.isbn).filter_by(
            launched=False).group_by(
            cls.isbn).limit(current_app.config['NUM_UPLOAD_BOOK']).all()
        recent_list = cls.__parse_group(recent_list)

        return recent_list

    @classmethod
    def __parse_group(cls, recent_list):
        return [isbn[0] for isbn in recent_list]
