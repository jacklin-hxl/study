from flask_login import login_user, login_required, logout_user

from . import web
from flask import render_template, request, redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.user import User
from app.models.base import db
from ..lib.email import send_mail


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
        user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if user:
            login_user(user)
            next_ = request.args.get("next")
            # 防止重定向攻击
            # e.g. http://127.0.0.1:5000/login/?next=https://www.baidu.com
            if next_ and next_.startswith("/"):
                return redirect(next_)
            return redirect(url_for("web.index"))
        else:
            flash("用户或密码错误")

    return render_template("auth/login.html", form=form)


@web.route("/forget/password/", methods=["GET", "POST"])
def forget_password_request():
    """
    发送充值密码至邮箱
    :return:
    """
    if request.method == "POST":
        form = EmailForm(request.form)
        if form.validate():
            # 查找指定的邮箱的用户是否存在，不存在提示该用户不存在
            # 发送重置链接到指定邮箱，链接里附带标识用户的加密字段，存在过期时间
            email = form.email.data
            user = User.query.filter_by(email=email).first_or_404()
            token = user.generate_token()
            send_mail(recipient=email, subject="[鱼书] Reset Password",
                      template="email/reset_password.html",
                      token=token,
                      user=user)
            flash("重置密码邮件已经发送到你的邮箱")

    return render_template("auth/forget_password_request.html")


@web.route("/pending/")
def pending():
    pass


@web.route("/personal_center/")
def personal_center():
    pass


@web.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("web.login"))


@web.route("/forget/password/<token>", methods=["GET", "POST"])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if form.validate():
        success = User.reset_password(token, form.new_password.data)
        if success:
            flash("password reset successful")
        else:
            flash("链接失效")
    return render_template("auth/forget_password.html", form=form)
