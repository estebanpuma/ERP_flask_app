from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))


class DefaultConfig:
    SECRET_KEY = "this123is456my789secret321key654"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # App environment
    APP_ENV_LOCAL = "local"
    APP_ENV_DEVELOPMENT = "development"
    APP_ENV_PRODUCTION = "production"
    
    # Media dir
    MEDIA_DIR = join(BASE_DIR, 'media')
    PROFILE_IMG_DIR = join(MEDIA_DIR, 'profile')
    
    # Server port cambiar a env
    FLASK_RUN_HOST='0.0.0.0'

    FLASK_RUN_PORT=5000
