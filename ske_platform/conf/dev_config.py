import os
from .base_config import BaseConfig


class DevConfig(BaseConfig):
    # Env settings
    FLASK_ENV = 'development'
    FLASK_DEBUG = True

    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BaseConfig.BASE_DIR, 'devel.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BaseConfig.BASE_DIR, 'devel_migrations')
