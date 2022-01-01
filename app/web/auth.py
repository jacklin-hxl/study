from . import web
from flask import render_template, request, redirect, url_for
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from app.models.base import db


@web.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User()
        user.set_attrs(**request.form)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("web.login"))
    return render_template("auth/register.html", form=form)


@web.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        pass
    return render_template("auth/login.html", form=form)


@web.route("/forget/", methods=["GET", "POST"])
def forget_password_request():
    form = LoginForm(request.form)

    return render_template("auth/forget_password_request.html", form=form)

@web.route("/")
def index():
    return redirect(url_for("web.login"))
