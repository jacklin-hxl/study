from flask import current_app
from flask_login import current_user

from .base import Base, db
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .wish import Wish


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
        sql = """
                select g1.isbn from gift as g1 left join
                (select substring_index(
                group_concat(tmp.id order by tmp.create_time desc), ',',1) as id
                from gift as tmp group by isbn)
                as g2 on g1.id=g2.id 
              """

        list_ = db.session.execute(sql).fetchall()
        recent_list = [{"isbn": isbn[0]} for isbn in list_]
        return recent_list

    @classmethod
    def in_gifts(cls, isbn):
        flag = False
        if current_user.is_authenticated:
            if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                    launched=False).first():
                flag = True

        return flag
