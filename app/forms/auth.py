from wtforms import StringField, PasswordField, Form, EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(Form):

    nickname = StringField(validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField(validators=[DataRequired(), Length(min=8, max=16)])
    email = EmailField(validators=[DataRequired()])
