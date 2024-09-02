from flask_wtf import FlaskForm

from wtforms import StringField, EmailField, PasswordField, SelectField, DateField, SubmitField, TextAreaField, RadioField, BooleanField
from wtforms.validators import Email, DataRequired, Optional

from app.models import Role, ClientCategory

from app.validations import validate_ruc_or_ci, validate_username, validate_ruc, validate_mobile_phone



class ClientForm(FlaskForm):
    client_type = RadioField(
        'Tipo de Cliente',
        choices=[('natural', 'Natural'), ('juridica', 'Jurídica')],
        validators=[DataRequired()]
    )
    ruc_or_ci = StringField('Cédula', validators=[DataRequired(message="Este campo es obligatorio."), validate_ruc_or_ci])
    is_ci = BooleanField('CI', validators=[Optional()])
    name = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio."), validate_username])
    address = StringField('Direccion', validators=[Optional()])
    phone = StringField('Teléfono', validators=[Optional(), validate_mobile_phone])
    email = EmailField('Email', validators=[Email(message="Ingrese un correo electrónico válido."), Optional()])
    category = SelectField('Categoria', choices=[('', 'Seleccione una categoria')], validators=[Optional()])

    submit = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.category.choices += [(c.id, c.name) for c in ClientCategory.query.all()]


class UpdateClientForm(ClientForm):
    def __init__(self, *args, **kwargs):
        super(UpdateClientForm, self).__init__(*args, **kwargs)
        self.password.validators = [Optional()]


class ClientCategoryForm(FlaskForm):
    name = StringField('Categoria', validators=[DataRequired(message="Este campo es obligatorio.")])
    description = TextAreaField('Descripción')
    submit = SubmitField('Guardar')