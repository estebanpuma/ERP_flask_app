from flask import render_template, redirect, url_for, flash

from app.models import Product, ProductCategory, ProductSubCategory

from . import production_bp


@production_bp.route('/production')
def production():

    return render_template('production/index.html')



