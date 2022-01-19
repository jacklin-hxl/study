from wtforms import StringField, PasswordField, Form, EmailField
from wtforms.validators import DataRequired, Length


class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired(), Length(max=10)])
    mobile = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    message = StringField(validators=[DataRequired()])
