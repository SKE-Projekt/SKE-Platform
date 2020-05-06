from flask import render_template, request, flash, redirect,abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from ske_platform.database import db
from . import auth, login_manager
from .forms import LoginForm, RegisterForm
from .models import User


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('login')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        flash('Musisz sie wylogować aby to zrobić!', 'warning is-light')
        return redirect('/')
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None:
            flash('Nie ma takiego użytkownika!', 'danger')
        else:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user)
                return redirect('/')
            else:
                flash('Złe hasło i/lub nazwa użytkownika!', 'danger')
    return render_template('auth/login.html', login_form=login_form)

@auth.route('/logout')
@login_required
def logout():
    try:
        logout_user()
    except:
        flash('Stało się coś złego, skontaktuj się z nami!', 'danger')
    finally:
        flash('Poprawnie wylogowano. Do zobaczenia!', 'success')
    return redirect('login')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        flash('Musisz sie wylogować aby to zrobić!', 'warning is-light')
        return redirect('/')

    register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate():
        if User.query.filter_by(username=register_form.username.data).first() != None:
            flash('Nazwa użytkownika jest już zajęta!', 'danger')
        else:
            user = User(password=generate_password_hash(register_form.password.data), username=register_form.username.data, email=register_form.email.data, first_name=register_form.first_name.data, last_name=register_form.last_name.data, is_superuser=False)
            db.session.add(user)
            db.session.commit()
            flash('Możesz się teraz zalogować!', 'success')
            return redirect('login')
    return render_template('auth/register.html', register_form=register_form)
