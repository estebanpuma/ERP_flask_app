from flask import current_app

from app.models import Product, ProductCategory, ProductSubCategory

from marshmallow import ValidationError


class ProductService:
    @staticmethod
    def create(data):
        category = ProductCategory.query.get(data['product-category'])
        sub_category = ProductSubCategory.query.get(data['product-sub_category'])
        if not category:
            raise ValidationError('Invalid category_id')
        if not sub_category:
            raise ValidationError('Invalid sub_category_id')

        product = Product(
            code=data['product-code'],
            name=data['product-name'],
            description=data['product-description'],
            category_id = data['product-category'],
            sub_category_id= data['product-sub_category']
            
        )
        success, error = product.save()
        if success:
            return product
        else:
            current_app.logger.warning(f'error al guardar producto nuevo. Msg: {error}')
            return error
        
    def update(product, data):

        category = ProductCategory.query.get(data['product-category'])
        sub_category = ProductSubCategory.query.get(data['product-sub_category'])
        if not category:
            raise ValidationError('Invalid category_id')
        if not sub_category:
            raise ValidationError('Invalid sub_category_id')

        product.code = data['product-code']
        product.name = data['product-name']
        product.description = data['product-description']
        product.category_id = data['product-category']
        product.sub_category_id = data['product-sub_category']

        success, error = product.save()


        if success:
            return True
        else:
            current_app.logger.warning(f'error al actualizar producto <id:{product.id}> msg: {error}')
            return False
        
    
    def disable(product_id):
        product = Product.query.get_or_404(product_id)
        product.is_deleted = True

    @staticmethod
    def get_product(product_id):
        return Product.query.get_or_404(product_id)

    @staticmethod
    def get_all_products():
        return Product.query.all()



#*****************************Linea/catgoria*****************************

class CategoryService:
    @staticmethod
    def create(data):
       

        category = ProductCategory(
            name=data['product-category-name'],
            description=data['product-category-description']            
        )
        success, error = category.save()
        if success:
            return category
        else:
            current_app.logger.warning(f'error al guardar nueva categoria. Msg: {error}')
            return error
        
    def update(category, data):

        category.code = data['product-category-code']
        category.name = data['product-category-name']
        category.description = data['product-category-description']


        success, error = category.save()

        if success:
            return True
        else:
            current_app.logger.warning(f'error al actualizar categoria <id:{category.id}> msg: {error}')
            return False
        
    
    def disable(category_id):
        category = ProductCategory.query.get_or_404(category_id)
        category.is_deleted = True

    @staticmethod
    def get_category(obj_id):
        return ProductCategory.query.get_or_404(obj_id)

    @staticmethod
    def get_all_categories():
        return ProductCategory.query.all()
    


#*****************************SUb linea**************************
class ProductSubCategoryService:
    @staticmethod
    def create(data):
       
        category = ProductCategory.query.get(data['product-sub-category-category'])
        
        if not category:
            raise ValidationError('Invalid category_id')
        
        sub_category = ProductSubCategory(
            name=data['product-sub-category-name'],
            description=data['product-sub-category-description'] ,
            category_id = data['product-sub-category-category']

        )
        success, error = sub_category.save()
        if success:
            return sub_category
        else:
            current_app.logger.warning(f'error al guardar nueva categoria. Msg: {error}')
            return error
        
    def update(sub_category, data):

       
        sub_category.name =data['product-sub-category-name']
        sub_category.description = data['product-sub-category-description']
        sub_category.category_id = data['product-sub-category-category']

        success, error = sub_category.save()

        if success:
            return True
        else:
            current_app.logger.warning(f'error al actualizar subcategoria <id:{sub_category.id}> msg: {error}')
            return False
        
    
    def disable(category_id):
        category = ProductSubCategory.query.get_or_404(category_id)
        category.is_deleted = True

    @staticmethod
    def get_sub_category(obj_id):
        return ProductSubCategory.query.get_or_404(obj_id)

    @staticmethod
    def get_all_sub_categories():
        return ProductSubCategory.query.all()
    