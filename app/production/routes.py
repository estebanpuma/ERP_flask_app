from flask import render_template, redirect, url_for, flash

from app.models import Product, ProductCategory, ProductSubCategory

from . import production_bp


@production_bp.route('/production')
def production():

    return render_template('production/production.html')


@production_bp.route('/product/list')
def products_view():
    title = 'Productos'
    products = Product.query.all()
    return render_template('production/products_view.html',
                           title = title,
                           products = products)


@production_bp.route('/product/<int:product_id>/view')
def product_view(product_id):
    title = 'Producto'
    product = Product.query.get_or_404()

    return render_template('production/product_view.html')


@production_bp.route('/product/add')
def add_product():
    title = 'Nuevo producto'
    return render_template('production.add_product.html',
                           title = title)
