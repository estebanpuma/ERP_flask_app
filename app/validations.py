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
    

def validate_mobile_phone(form, field):
    phone = field.data
    if not phone.isdigit():
        raise ValidationError('Numero celular contener solo números.')
    if len(phone) != 10:
        raise ValidationError('El número debe tener exactamente 10 dígitos.')
    

def validate_username(form, field):
    username = field.data
    if len(username) < 3:
        raise ValidationError('El nombre debe tener al menos 3 caracteres')


def validate_ruc(form, field):
    ruc = field.data
    if not ruc.isdigit():
        raise ValidationError('El RUC debe contener solo números.')
    if len(ruc) != 13:
        raise ValidationError('El RUC debe tener exactamente 13 dígitos.')


def validate_ruc_or_ci(form, field):
    ruc_or_ci = field.data

    if not ruc_or_ci.isdigit():
        raise ValidationError('El RUC/CI debe contener solo números.')
    
    if form.client_type.data == 'natural':
        if form.is_ci.data:  # Si es una cédula
            if len(ruc_or_ci) != 10:
                raise ValidationError('La cédula debe tener 10 dígitos.')
        else:  # Si es un RUC de persona natural
            if len(ruc_or_ci) != 13:
                raise ValidationError('El RUC debe tener 13 dígitos.')
    elif form.client_type.data == 'juridica':  # RUC de persona jurídica
        if len(ruc_or_ci) != 13:
            raise ValidationError('El RUC debe tener 13 dígitos para personas jurídicas.')