from flask import request, render_template, redirect, url_for, flash, request, session, jsonify, current_app

from app.models import Product, ProductCategory, ProductSubCategory

from app.utils import update_form_choices

from .forms import ProductForm, ProductCategoryForm, ProductSubCategoryForm

from . import products_bp

import requests

API_BASE_URL = "http://localhost:5000/api"

#****************Productos*********************************#

@products_bp.route('/product/view')
def view_products():
    title = 'Productos'
    prev_url = url_for('production.production')
    #products = Product.query.all()
    current_app.logger.info('ingresa a productVieeew')
    response = requests.get(f"{API_BASE_URL}/products")
    current_app.logger.info('Obitnen product')
    products = response.json()
    current_app.logger.info('serializa prdcut')
    
    return render_template('products/view_products.html',
                           title = title,
                           products = products,
                           prev_url = prev_url)


@products_bp.route('/product/<int:product_id>/view')
def view_product(product_id):
    title = 'Producto'
    prev_url = url_for('products.view_products')
    #product = Product.query.get_or_404(product_id)
    response = requests.get(f"{API_BASE_URL}/products/{product_id}")
    product = response.json()

    return render_template('products/view_product.html',
                           title = title,
                           product = product,
                           prev_url = prev_url)


@products_bp.route('/product/add', methods=['GET', 'POST'])
def add_product():
    title = 'Nuevo producto'
    prev_url = url_for('products.view_products')
    form = ProductForm(prefix='product')
    formCategory = ProductCategoryForm(prefix='product-category')
    formSubCategory = ProductSubCategoryForm(prefix='product-sub-category')

    # Verificar si el formulario de producto fue enviado
    if 'product-submit' in request.form and form.validate_on_submit():

        form_data = request.form.to_dict()
        
        response = requests.post(f"{API_BASE_URL}/products",json=form_data)
        response = response.json()
        
        if response==200:
            flash('Producto añadido con éxito', 'success')    
            return redirect(url_for('products.view_products'))
        else:
            flash(f'Error, no se pudo guardar producto', "danger")
        
    # Verificar si el formulario de subcategoría fue enviado
    elif 'product-sub-category-submit' in request.form and formSubCategory.validate_on_submit():
        form_data = request.form.to_dict()
        
        response = requests.post(f"{API_BASE_URL}/subcategory",json=form_data)
        response = response.json()
        
        if response==200:
            update_form_choices(form.category, ProductCategory)
            update_form_choices(form.sub_category, ProductSubCategory)
            update_form_choices(formSubCategory.category, ProductCategory)
            flash('SubLinea agragada con éxito', 'success')    
        else:
            flash(f'Error, no se pudo guardar Sublinea', "danger")

    # Verificar si el formulario de categoría fue enviado
    elif 'product-category-submit' in request.form and formCategory.validate_on_submit():
        form_data = request.form.to_dict()
        
        response = requests.post(f"{API_BASE_URL}/category",json=form_data)
        response = response.json()
        
        if response==200:
            update_form_choices(form.category, ProductCategory)
            update_form_choices(formSubCategory.category, ProductCategory)
            flash('Linea agragada con éxito', 'success')    
        else:
            flash(f'Error, no se pudo guardar line', "danger")
       
            

    
    return render_template('products/add_product.html',
                           title=title,
                           prev_url=prev_url,
                           form=form,
                           formSubCategory=formSubCategory,
                           formCategory=formCategory)



#*********************Categorias/Lineas************************************

@products_bp.route('/product_category/view')
def view_product_categories():
    title = 'Categorias'
    prev_url = url_for('products.view_products')
    products = Product.query.all()
    return render_template('products/view_product_categories.html',
                           title = title,
                           products = products,
                           prev_url = prev_url)


@products_bp.route('/category/<int:product_category_id>/view')
def view_product_category(product_category_id):
    title = 'Categoria'
    prev_url = url_for('products.view_categories')
    category = ProductCategory.query.get_or_404(product_category_id)

    return render_template('products/view_category.html',
                           title = title,
                           prev_url = prev_url,
                           category = category)


@products_bp.route('/product_category/add')
def add_product_category():
    title = 'Nueva categoria'
    prev_url = url_for('products.view_product_categories')
    return render_template('products/add_product_category.html',
                           title = title,
                           prev_url = prev_url)


#*********************Subcategorias/Sublinea******************

@products_bp.route('/product_sub_category/view')
def view_product_sub_categories():
    title = 'Categorias'
    prev_url = url_for('products.view_products')
    subcategories = ProductSubCategory.query.all()
    return render_template('products/view_product_sub_categories.html',
                           title = title,
                           subcategories = subcategories,
                           prev_url = prev_url)


@products_bp.route('/product_sub_category/<int:product_sub_category_id>/view')
def view_product_sub_category(product_sub_category_id):
    title = 'Sub Categoria'
    prev_url = url_for('products.view_categories')
    category = ProductSubCategory.query.get_or_404(product_sub_category_id)

    return render_template('products/view_product_sub_category.html',
                           title = title,
                           prev_url = prev_url,
                           category = category)


@products_bp.route('/product_sub_category/add')
def add_product_sub_category():
    title = 'Nueva categoria'
    prev_url = url_for('products.view_categories')
    return render_template('products/add_product_sub_category.html',
                           title = title,
                           prev_url = prev_url)