from flask import redirect, flash

from app.models import User, Role


def update_user(user, form):
    # Obtener los datos del formulario
    username = form.username.data
    ci = form.ci.data
    email = form.email.data
    password = form.password.data
    role_id = form.role.data
    role = Role.query.get(role_id)
    birthday = form.birthday.data

    # Actualizar los atributos del usuario existente
    user.username = username
    user.ci = ci
    user.email = email
    user.birthday = birthday

    # Actualizar los roles del usuario
    user.roles = [role]  # Asigna un nuevo rol, reemplazando los anteriores.

    # Si se ingresó una nueva contraseña actualizar
    if password:
        user.set_password(password)

    # Guardar los cambios en la base de datos
    if user.save():
        return True
    else:
        return False