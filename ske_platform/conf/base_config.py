import os


BASE_DIR_FLAT = os.path.abspath(os.path.dirname(__name__))

class BaseConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__name__))
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Ed settings
    ED_BINARY = os.path.join(BASE_DIR_FLAT, '../Edlang/bin/edlang')

    # Database settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
