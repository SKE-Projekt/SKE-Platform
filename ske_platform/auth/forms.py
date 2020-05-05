from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(label='Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField(label='Hasło', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField(label='Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField(label='Hasło', validators=[DataRequired()])

    email = EmailField(label='Adres email', validators=[DataRequired()])
    first_name = StringField(label='Imię', validators=[DataRequired()])
    last_name = StringField(label='Nazwisko', validators=[DataRequired()])
