from . import web
from flask import render_template, request, redirect, url_for
from app.forms.auth import RegisterForm
from app.models.user import User
from app.models.base import db

@web.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User()
        user.set_attrs(request.form)
        db.session.add(user)
        db.session.commit()
        return redirect("https://www.baidu.com")
    return render_template("auth/register.html", form=form)

@web.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")