from flask import current_app, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required

from app.forms.drift import DriftForm
from app.lib import enums
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookSingle
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


@web.route("/send/drift/<gid>", methods=["POST", "GET"])
@login_required
def send_drift(gid):
    # fixme 这里会重复添加交易
    form = DriftForm(request.form)
    gifter = Gift.query.get_or_404(gid)
    # wish = Wish.query.filter_by(uid=current_user.id, isbn=gift.isbn)
    requestor = User.query.get_or_404(current_user.id)
    if not gifter.requestor_in_gift(current_user.id):
        flash("用户不能自己赠送自己")
        return redirect(url_for("web.book_detail", isbn=gifter.isbn))

    if not requestor.can_drift():
        flash("鱼豆不足")
        return render_template("not_enough_beans.html", beans=requestor.beans)

    if request.method == "POST":

        populate_drift(form=form, gifter=gifter, requestor=requestor,
                       pending=enums.PENDING.STATUS_TRADING.value)
        flash("提交成功")
        return redirect(url_for("web.book_detail", isbn=gifter.isbn))

    return render_template("drift.html", gifter=gifter.user, user_beans=requestor.beans, form=form)


@web.route("/satisfy/<isbn>/<wid>")
def satisfy_wish(isbn, wid):
    pass


@web.route("/wish/redraw/<wid>")
def redraw_from_wish(wid):
    Wish.revoke_wish(wid=wid)
    return "ok"


def populate_drift(form, gifter, requestor, pending):
    with db.auto_commit():
        drift = Drift()
        form.populate_obj(drift)

        drift.giver_id = gifter.user.id
        drift.giver_name = gifter.user.nickname

        drift.supplicant_id = requestor.id
        drift.supplicant_name = requestor.nickname

        book = BookSingle(YuShuBook().search_by_isbn(gifter.isbn).first)
        drift.isbn = book.isbn
        drift.book_title = book.title
        drift.book_author = book.author
        drift.img = book.image

        drift.pending = pending

        drift.gift_id = gifter.id
        db.session.add(drift)




