from flask import current_app
from flask_login import login_required, current_user

from . import web
from ..models.base import db
from ..models.gift import Gift


@web.route("/my/gifts/")
@login_required
def my_gifts():
    return "my gift"


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


