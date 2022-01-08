from sqlalchemy import Column, String, Integer

from .base import Base
from flask_login import UserMixin

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

@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)
