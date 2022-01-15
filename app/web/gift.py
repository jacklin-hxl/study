from flask import current_app, render_template
from flask_login import login_required, current_user

from . import web
from ..models.base import db
from ..models.gift import Gift
from ..spider.yushu_book import YuShuBook
from ..view_models.book import BookSingle
from ..view_models.inventory import Inventory


@web.route("/my/gifts/")
@login_required
def my_gifts():
    gifts = Gift.get_user_gifts()
    inventory = Inventory(gifts)
    return render_template("my_gifts.html", gifts=inventory.details)


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


@web.route("/gift/redraw/<gid>")
@login_required
def redraw_from_gifts(gid):
    Gift.revoke_gift(gid)
    return 'ok'
