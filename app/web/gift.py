
from . import web
from flask_login import login_required, current_user

from ..models.base import db
from ..models.gift import Gift


@web.route("/my/gifts/")
@login_required
def my_gifts():
    return "my gift"


@web.route("/gifts/book/<isbn>")
@login_required
def save_to_gifts(isbn):
    if Gift.query.filter_by(uid=current_user.id, isbn=isbn).first():
        return "已经赠送"
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    db.session.add(gift)
    db.session.commit()
    return "ok"
