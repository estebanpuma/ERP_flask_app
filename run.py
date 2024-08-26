import os

from dotenv import load_dotenv

from config.development import DevelopmentConfig
from config.production import ProductionConfig

from app import create_app




load_dotenv()

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

# Obtener el nombre del módulo de configuración desde la variable de entorno
config_name = os.getenv('APP_SETTINGS_MODULE')
print(config_name)
# Crear la aplicación Flask usando la configuración especificada
app = create_app(config_by_name[config_name])


if __name__ == '__main__':
    app.run()