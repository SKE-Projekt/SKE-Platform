from flask import render_template

from . import auth, login_manager
from .forms import LoginForm


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@auth.route('/login')
def login():
    login_form = LoginForm()
    return render_template('auth/login.html', login_form=login_form)
