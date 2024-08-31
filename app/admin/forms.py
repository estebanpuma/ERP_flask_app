from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, SelectField, DateField, SubmitField, TextAreaField
from wtforms.validators import Email, DataRequired, Optional

from app.models import Role

from .validations import no_admin, validate_ci


class SignupForm(FlaskForm):
    ci = StringField('Cédula', validators=[DataRequired(message="Este campo es obligatorio."), validate_ci])
    username = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio."), no_admin])
    email = EmailField('Email', validators=[Email(message="Ingrese un correo electrónico válido."), DataRequired(message="Este campo es obligatorio.")])
    password = PasswordField('Password', validators=[DataRequired(message="Este campo es obligatorio.")])
    #confirm_password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Cargo', choices=[('', 'Seleccione un cargo')])
    birthday = DateField('Fecha de nacimiento', validators=[Optional()])
    submit = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.role.choices += [(c.id, c.name) for c in Role.query.all()]


class RoleForm(FlaskForm):
    name = StringField('Cargo', validators=[DataRequired(message="Este campo es obligatorio.")])
    description = TextAreaField('Descripción')
    submit = SubmitField('Guardar')