from math import floor

from flask import current_app
from sqlalchemy import Column, String, Integer

from .base import Base, db
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired

from .gift import Gift
from .wish import Wish
from .. import login_manager
from ..lib.helper import is_isbn_or_key
from ..spider.yushu_book import YuShuBook


class User(UserMixin, Base):

    __tablename__ = "user"

    password = Column(type_=String(50), nullable=False)
    nickname = Column(type_=String(20), nullable=False)
    email = Column(type_=String(20))
    beans = Column(Integer, server_default='0')

    # 校验isbn格式
    # 校验isbn是否存在
    # 一个用户不可添加同一个isbn
    # 一个用户不可既是该书籍赠送者也是索要者
    #  既不再赠送清单也不在心愿清单
    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != "isbn":
            return False
        elif YuShuBook().search_by_isbn(isbn).total <= 0:
            return False
        gift = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wish = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if gift or wish:
            return False
        return True

    def generate_token(self, expiration=300):
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        token = s.dumps({"uid": self.id}).decode("utf-8")
        return token

    # 判断用户的beans是否达到索要要求
    # 用户 beans 大于 0
    # 用户 需要每赠送两次，才能索要一次
    def can_drift(self):
        if self.beans < 1:
            return False
        success_gifts_count = Gift.query.filter_by(id=self.id, launched=True).count()
        success_wishes_count = Wish.query.filter_by(id=self.id, launched=True).count()
        if floor(success_gifts_count / 2) < success_wishes_count:
            return False
        return True


    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            u = s.loads(token)
            uid = u.get("uid")
            user = User.query.get(uid)
            if user:
                sql = f"""update user set password={new_password} where id={uid}"""
                with db.auto_commit():
                    db.session.execute(sql)
                return True
        except SignatureExpired as e:
            print("Signature Expired")
            return False

    @classmethod
    def get_user_by_gid(cls, gid):
        gift = Gift.query.filter_by(id=gid).first()
        gifter = User.query.filter_by(id=gift.uid).first()
        return gifter



@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
