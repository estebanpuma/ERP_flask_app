import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logging(app):
    """Configura el sistema de logging para la aplicación Flask."""
    
    # Establecer el nivel de logging para la aplicación
    app.logger.setLevel(logging.INFO)

    # Crear un manejador de archivo de log con rotación
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
    
    # Formateador de log
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))

    # Establecer el nivel del manejador de archivo
    file_handler.setLevel(logging.INFO)
    
    # Agregar el manejador al logger de la aplicación
    app.logger.addHandler(file_handler)

    # Log inicial para indicar que la configuración de logging está lista
    app.logger.info('Sistema de logging configurado')