from flask import Flask, render_template

from flask_restful import Api

from flask_marshmallow import Marshmallow 

from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from jinja2 import TemplateNotFound


db = SQLAlchemy()

migrate = Migrate()

ma = Marshmallow()

api = Api()

login_manager = LoginManager()


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    #Rutas para APIs
    from app.resources.product_api import ProductResource, CategoryResource, ProductSubCategoryResource
    api.add_resource(ProductResource, '/api/products', '/api/products/<int:product_id>')
    api.add_resource(CategoryResource, '/api/category', '/api/category/<int:category_id>')
    api.add_resource(ProductSubCategoryResource, '/api/subcategory', '/api/subcategory/<int:subcategory_id>')

    api.init_app(app)
    from .logs import setup_logging
    setup_logging(app)
    
    with app.app_context():
        from .models import initialize_admin_user  
        #initialize_admin_user()

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .crm import crm_bp
    app.register_blueprint(crm_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .production import production_bp
    app.register_blueprint(production_bp)

    from .products import products_bp
    app.register_blueprint(products_bp)

    from .sales import sales_bp
    app.register_blueprint(sales_bp)

    from .users import users_bp
    app.register_blueprint(users_bp)



    

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
    
