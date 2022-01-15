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
        """
        return
        e.g.
            [{"isbn":111111111},{"isbn":222222}]
        """
        sql = """
                select g1.isbn from gift as g1 right join
                (select substring_index(
                group_concat(tmp.id order by tmp.create_time desc), ',',1) as id
                from gift as tmp where status=1 group by isbn)
                as g2 on g1.id=g2.id
                """

        return db.session.execute(sql).mappings()

    @classmethod
    def in_gifts(cls, isbn):
        flag = False
        if current_user.is_authenticated:
            if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                    launched=False).first():
                flag = True
        return flag

    @classmethod
    def get_user_gifts(cls):
        # todo 需要返回gift id
        sql = f"""
                select g.isbn, count(w.isbn) as count, any_value(g.id) as id from
                wish w right join(select isbn, id from gift where uid = 1 and status=1) as g 
                on g.isbn = w.isbn and w.status=1
                group by g.isbn;
                """
        return db.session.execute(sql).mappings()

    @classmethod
    def revoke_gift(cls, gid):
        sql = f"update gift set status=0 where id = {gid} and status=1 and uid={current_user.id};"
        with db.auto_commit():
            db.session.execute(sql)
