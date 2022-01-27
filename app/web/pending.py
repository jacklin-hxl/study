from flask import render_template
from sqlalchemy import or_

from . import web
from flask_login import login_required, current_user

from ..models.drift import Drift


@web.route("/pending/")
@login_required
def pending():
    """
    获取用户的历史交易记录
    索要的记录和赠送的记录
    """
    drifts = Drift.query.filter(
        or_(Drift.giver_id == current_user.id, Drift.supplicant_id == current_user.id)).all()
    return render_template("pending.html", drifts=drifts)