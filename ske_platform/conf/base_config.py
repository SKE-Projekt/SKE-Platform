import os


class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__name__))
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
