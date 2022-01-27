from flask_login import current_user
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base, db


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

    @classmethod
    def get_user_wishes(cls):
        # todo 需要返回wish id
        sql = f"""
                select w.isbn, count(g.isbn) as count, any_value(w.id) as id 
                from gift as g 
                right join 
                (select isbn, id from wish where uid = {current_user.id} and status=1 order by create_time) as w
                on w.isbn=g.isbn and status=1 and launched=False
                group by w.isbn
                """
        return db.session.execute(sql).mappings()

    @classmethod
    def revoke_wish(cls, wid):
        sql = f"""update wish set status=0 where uid = {current_user.id} and status=1 and id={wid}"""
        with db.auto_commit():
            db.session.execute(sql)