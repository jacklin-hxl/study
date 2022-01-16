from flask import current_app, render_template
from flask_login import current_user, login_required

from app.models.base import db
from app.models.wish import Wish
from app.view_models.inventory import Inventory
from app.web import web


@web.route("/wish/book/<isbn>")
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            current_user.beans += current_app.config["BEANS_UPLOAD_ONE_BOOK"]
            db.session.add(wish)
        return "ok"
    return "false"


@web.route("/my/wish/")
def my_wish():
    wishes = Wish.get_user_wishes()
    inventory = Inventory(wishes)

    return render_template("my_wish.html", wishes=inventory.details)


@web.route("/send/drift/<gid>")
def send_drift(gid):
    pass

@web.route("/satisfy/<isbn>/<wid>")
def satisfy_wish(isbn, wid):
    pass

@web.route("/wish/redraw/<wid>")
def redraw_from_wish(wid):
    Wish.revoke_wish(wid=wid)
    return "ok"
