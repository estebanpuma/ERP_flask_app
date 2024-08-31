from flask import redirect, flash

from app.models import User, Role


def save_user(form):
    username = form.username.data
    ci = form.ci.data
    email = form.email.data
    password = form.password.data
    role_id = form.role.data
    role = Role.query.get(role_id)
    birthday = form.birthday.data

    user = User(username = username,
                ci = ci,
                email = email,
                birthday = birthday)
    
    user.roles.append(role)
    
    user.set_password(password)

    if user.save():
        return True
        

    else:
        return False
        