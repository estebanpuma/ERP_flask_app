from flask import render_template, redirect, url_for, flash

from flask_login import login_required

from app.models import User, Role, Permission

from .utils import save_user

from .forms import SignupForm, RoleForm
from . import admin_bp


@admin_bp.route('/user/view')
def view_users():
    title = 'Usuarios'
    prev_url = url_for('public.index')
    users = User.query.all()
   
    return render_template('admin/view_users.html',
                           title = title,
                           users = users,
                           prev_url = prev_url)


@admin_bp.route('/user/add', methods=['GET', 'POST'])
@login_required
def add_user():
    title = 'Nuevo Usuario'
    prev_url = url_for('admin.view_users')
    form = SignupForm()
    
    if form.validate_on_submit():

        if save_user(form):
            flash('Usuario guardado exitosamente', 'success')
        else:
            flash('Ocurrio un error al intenar guardar', 'danger')

        return redirect(url_for('admin.view_users'))

    return render_template('admin/add_user.html',
                           title = title,
                           form = form,
                           prev_url = prev_url)


@admin_bp.route('/role/view')
def view_roles():
    title = 'Roles'
    prev_url = url_for('public.index')
    roles= Role.query.all()

    return render_template('admin/view_roles.html',
                           title = title,
                           roles = roles,
                           prev_url = prev_url)


@admin_bp.route('/role/add', methods=['GET', 'POST'])
@login_required
def add_role():
    title = 'Nuevo rol'
    prev_url = url_for('admin.view_roles')
    form = RoleForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        role = Role(name=name, description=description)

        if role.save():
            flash("Cargo guardado exitosamente", 'success')
        else:
            flash("Hubo un problema al intentar guardar", 'danger')
        
        return redirect(url_for('admin.view_roles'))

    return render_template('admin/add_role.html',
                           title = title,
                           form = form,
                           prev_url = prev_url)