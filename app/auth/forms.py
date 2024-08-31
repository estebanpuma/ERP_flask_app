from flask_wtf import FlaskForm

from wtforms import SubmitField, EmailField, PasswordField, StringField, DateField, SelectField, BooleanField

from wtforms.validators import Email, DataRequired




class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email(message="Ingrese un correo electrónico válido."), DataRequired(message="Este campo es obligatorio.")])
    password = PasswordField('Password', validators=[DataRequired(message="Este campo es obligatorio.")])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Login')




