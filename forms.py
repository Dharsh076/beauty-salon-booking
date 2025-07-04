from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    service = StringField("Service", validators=[DataRequired()])
    datetime = StringField("Date and Time", validators=[DataRequired()])
    submit = SubmitField("Book")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
