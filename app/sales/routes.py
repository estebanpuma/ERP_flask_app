from flask import redirect, render_template, flash, url_for

from flask_login import current_user


from . import sales_bp


@sales_bp.route('/sale_order/add')
def add_sale_order():
    title = 'Nueva Orden de compra'
    prev_ref = url_for('crm.crm')
    return render_template('sales/add_sale_order.html')