from wtforms.validators import ValidationError


def no_admin(form, field):
    if 'admin' in field.data.lower():
        raise ValidationError('El nombre de usuario no puede contener "admin".')
    


def validate_ci(form, field):
    cedula = field.data
    if not cedula.isdigit():
        raise ValidationError('La cédula debe contener solo números.')
    if len(cedula) != 10:
        raise ValidationError('La cédula debe tener exactamente 10 dígitos.')