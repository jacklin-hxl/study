from wtforms import StringField, PasswordField, Form, EmailField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models.user import User


class AuthBase(Form):
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=16)])
    email = EmailField(validators=[DataRequired()])


class RegisterForm(AuthBase):
    nickname = StringField(validators=[DataRequired(), Length(min=3, max=10)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已经注册过！")

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError("用户名已经使用过！")


class LoginForm(AuthBase):
    pass