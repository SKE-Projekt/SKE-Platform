import os

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(os.getenv('CONFIG_CLASS'))

from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)

from .database import db
db.init_app(app)
mg = Migrate(app, db)

from .auth import auth
app.register_blueprint(auth)

from .auth import login_manager
login_manager.init_app(app)

@app.route('/')
def landing():
    return render_template('ske/landing.html')
