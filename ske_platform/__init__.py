import os

from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(os.getenv('CONFIG_CLASS'))

from .database import db
db.init_app(app)
mg = Migrate(app, db)

from .auth import auth
app.register_blueprint(auth)
