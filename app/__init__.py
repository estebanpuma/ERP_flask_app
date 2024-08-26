from flask import Flask, render_template
from jinja2 import TemplateNotFound

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app


def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler():
        return render_template('500.html'), 500
    
    @app.errorhandler(404)
    def error_404_handler():
        return render_template('404.html'), 404
    
    @app.errorhandler(TemplateNotFound)
    def handle_template_not_found():
         return render_template('error.html', message="Lo sentimos, la página que buscas no se pudo encontrar."), 404