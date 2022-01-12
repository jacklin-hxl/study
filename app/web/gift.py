from flask import current_app
from flask_login import login_required, current_user

from . import web
from ..models.base import db
from ..models.gift import Gift
from ..spider.yushu_book import YuShuBook
from ..view_models.book import BookSingle


@web.route("/my/gifts/")
@login_required
def my_gifts():
    gifts = Gift.get_user_gifts()
    gifts_ = []
    for gift in gifts:
        single = BookSingle(YuShuBook().search_by_isbn(gift["isbn"]).books)
        gifts_.append(single)


@web.route("/gifts/book/<isbn>")
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config["BEANS_UPLOAD_ONE_BOOK"]
            db.session.add(gift)
        return "ok"
    return "false"


