from flask import render_template, current_app

from . import public_bp

@public_bp.route('/')
def index():
    title = "Guifer"
    current_app.logger.info('Página de inicio accedida')
    return render_template('public/index.html',
                           title = title)