from flask import render_template, redirect, url_for, flash

from flask_login import login_required

from app.models import User, Role, Permission

from .utils import save_user

from .forms import SignupForm, RoleForm
from . import admin_bp


@admin_bp.route('/users_view')
def users_view():
    title = 'Usuarios'

    users = User.query.all()


   

    return render_template('admin/users_view.html',
                           title = title,
                           users = users)


@admin_bp.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    title = 'Nuevo Usuario'
    form = SignupForm()
    
    if form.validate_on_submit():

        if save_user(form):
            flash('Usuario guardado exitosamente', 'success')
        else:
            flash('Ocurrio un error al intenar guardar', 'danger')

        return redirect(url_for('admin.users_view'))

    return render_template('admin/add_user.html',
                           title = title,
                           form = form)


@admin_bp.route('/roles_view')
def roles_view():
    title = 'Roles'

    roles= Role.query.all()

    return render_template('admin/roles_view.html',
                           title = title,
                           roles = roles)


@admin_bp.route('/add_role', methods=['GET', 'POST'])
@login_required
def add_role():
    title = 'Nuevo rol'
    form = RoleForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        role = Role(name=name, description=description)

        if role.save():
            flash("Cargo guardado exitosamente", 'success')
        else:
            flash("Hubo un problema al intentar guardar", 'danger')
        
        return redirect(url_for('admin.roles_view'))

    return render_template('admin/add_role.html',
                           title = title,
                           form = form)