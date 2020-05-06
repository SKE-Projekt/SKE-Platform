from flask import Blueprint


sandbox = Blueprint('sandbox', __name__)

from .routes import *
