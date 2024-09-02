from flask import render_template, redirect, flash, request, url_for

from flask_login import login_required, current_user

from app.models import User

from app.admin.forms import UpdateUserForm

from .utils import update_user

from . import users_bp


@users_bp.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)

    title = 'Perfil'

    return render_template('users/profile.html',
                           title = title,
                           user = user)



@users_bp.route('/profile_edition/<int:user_id>', methods=['GET', 'POST'])
@login_required
def profile_edition(user_id):

    if current_user.id == int(user_id) or current_user.has_role('admin'):

        user = User.query.get_or_404(user_id)
    
    else:
        flash('No posee los permisos necesarios para realizar la accion', 'warning')
        return redirect(url_for('users.profile', user_id=current_user.id))

    form = UpdateUserForm(obj=user)
    title = 'Editar perfil'

    if form.validate_on_submit():

        if update_user(user=user, form=form):
            flash("Perfil actualizado", 'success')
            
        else:
            flash('Ocurrio un error', 'danger')

        return redirect(url_for('users.profile', user_id = user.id))
    
    return render_template('users/profile_edition.html',
                           title = title,
                           user = user,
                           form = form)