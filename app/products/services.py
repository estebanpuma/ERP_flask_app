from flask import current_app

from app.models import Product, ProductCategory, ProductSubCategory

from marshmallow import ValidationError


class ProductService:
    @staticmethod
    def create_product(product_data):
        category = ProductCategory.query.get(product_data['product-category'])
        sub_category = ProductSubCategory.query.get(product_data['product-sub_category'])
        if not category:
            raise ValidationError('Invalid category_id')
        if not sub_category:
            raise ValidationError('Invalid sub_category_id')

        product = Product(
            code=product_data['product-code'],
            name=product_data['product-name'],
            description=product_data['product-description'],
            category_id = product_data['product-category'],
            sub_category_id=product_data['product-sub_category']
            
        )
        success, error = product.save()
        if success:
            return product
        else:
            current_app.logger.warning(f'error al guardar producto nuevo. Msg: {error}')
            return error
        
    def update_product(product, product_data):

        category = ProductCategory.query.get(product_data['product-category'])
        sub_category = ProductSubCategory.query.get(product_data['product-sub_category'])
        if not category:
            raise ValidationError('Invalid category_id')
        if not sub_category:
            raise ValidationError('Invalid sub_category_id')

        product.code = product_data['product-code']
        product.name = product_data['product-name']
        product.description = product_data['product-description']
        product.category_id = product_data['product-category']
        product.sub_category_id = product_data['product-sub_category']

        success, error = product.save()

        if success:
            return True
        else:
            current_app.logger.warning(f'error al actualizar producto <id:{product.id}> msg: {error}')
            return False
        
    
    def disable_product(product_id):
        product = Product.query.get_or_404(product_id)

        product.is_deleted = True

    @staticmethod
    def get_product(product_id):
        return Product.query.get_or_404(product_id)

    @staticmethod
    def get_all_products():
        return Product.query.all()






    

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