import os

from .default import DefaultConfig, BASE_DIR


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "schema.db")







