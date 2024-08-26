from .default import DefaultConfig

class ProductionConfig(DefaultConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/production_db'
