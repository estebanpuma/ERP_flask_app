from flask import render_template, redirect, url_for, flash, request

from flask_login import login_user, logout_user, current_user

from app import login_manager

from app.models import User

from .forms import LoginForm

from . import auth_bp


@auth_bp.route('/login',methods = ['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    
    title = 'Login'
    form = LoginForm()
    emailErrorMsg = None
    passwordErrorMsg = None


    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            print(user.check_password(form.password.data),form.password.data)
            if user.check_password(form.password.data):

                login_user(user, remember=form.remember_me.data)

                next_page = request.args.get('next', None)
                
                if not next_page:
                    next_page = url_for("public.index")
                
                return redirect(next_page)
            
            else:
                passwordErrorMsg ='Contraseña incorrecta'
        
        else: 
            emailErrorMsg = 'Email incorrecto'
        

    return render_template('auth/login.html',
                    title = title,
                    form = form,
                    login = True,
                    emailErrorMsg = emailErrorMsg,
                    passwordErrorMsg = passwordErrorMsg)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))