from flask import current_app

from app.models import Product, ProductCategory, ProductSubCategory


def save_product(form):

    code = form.code.data
    name = form.name.data
    description = form.description.data
    category_id = form.category.data
    sub_category_id = form.sub_category.data

    product = Product(
        code = code,
        name = name,
        description = description,
        category_id = category_id,
        sub_category_id = sub_category_id
    )

    success, error = product.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'error al guardar producto nuevo. Msg: {error}')
        return False


def update_product(form, product):

    product.code = form.code.data
    product.name = form.name.data
    product.description = form.description.data
    product.category_id = form.category.data
    product.sub_category_id = form.sub_category.data

    success, error = product.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'error al actualizar producto <id:{product.id}> msg: {error}')
        return False
    

def save_product_category(form):
    
    name = form.name.data
    description = form.description.data

    category = ProductCategory(
        name = name,
        description = description
    )

    success, error = category.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'Error al guardar nueva categoria. Msg:{error}')


def update_product_category(form, category):
    
    category.name = form.name.data
    category.description = form.description.data

    success, error = category.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'Error al actualizar categoria <id:{category.id}>. Msg:{error}')


def save_product_sub_category(form):
    
    name = form.name.data
    description = form.description.data
    category_id = form.category.data

    sub_category = ProductSubCategory(
        name = name,
        description = description,
        category_id = category_id
    )

    success, error = sub_category.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'Error al guardar nueva subcategoria. Msg:{error}')


def update_product_sub_category(form, sub_category):
    
    sub_category.name = form.name.data
    sub_category.description = form.description.data
    sub_category.category_id = form.category.data

    success, error = sub_category.save()

    if success:
        return True
    else:
        current_app.logger.warning(f'Error al actualizar subcategoria <id:{sub_category.id}>. Msg:{error}')