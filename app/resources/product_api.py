from flask_restful import Resource, reqparse

from app.models import Product

from flask import jsonify, flash, json, request

from app.products.services import ProductService, CategoryService, ProductSubCategoryService

from app.schemas.product import ProductSchema, ProductCategorySchema, ProductSubCategorySchema

from app.products.forms import ProductForm


from flask import current_app

class ProductResource(Resource):
    def get(self, product_id=None):
        current_app.logger.info('ingresa a productResource')
        if product_id:
            product = ProductService.get_product(product_id)
            return ProductSchema().dump(product)
        
        products = ProductService.get_all_products()
        products = [ProductSchema().dump(product) for product in products ]
        
        return products
    
    def post(self):

         # Datos enviados por el cliente
        data = request.get_json()
        try:
            ProductService.create(data)  # Guardar producto si la validación es exitosa
            return jsonify(200)
        except:
            return jsonify(400)



class CategoryResource(Resource):
    def get(self, obj_id=None):
        print('**************ingresa a product cateoey resource**********')
        if obj_id:
            category = CategoryService.get_category(obj_id)
            return ProductCategorySchema().dump(category)                                                                                                          
        
        categories = CategoryService.get_all_categories()
        categories = [ProductCategorySchema().dump(obj) for obj in categories ]
        return categories
    
    def post(self):
        print('gole')

         # Datos enviados por el cliente
        data = request.get_json()
        try:
            CategoryService.create(data)  # Guardar producto si la validación es exitosa
            return jsonify(200)
        except:
            return jsonify(400)
        

class ProductSubCategoryResource(Resource):
    def get(self, obj_id=None):
        print('**************ingresa a product cateoey resource**********')
        if obj_id:
            sub_category = ProductSubCategoryService.get_sub_category(obj_id)
            return ProductCategorySchema().dump(sub_category)                                                                                                          
        
        sub_categories = ProductSubCategoryService.get_all_sub_categories()
        sub_categories = [ProductSubCategorySchema().dump(obj) for obj in sub_categories ]
        return sub_categories
    
    def post(self):
        print('gole')

         # Datos enviados por el cliente
        data = request.get_json()
        try:
            ProductSubCategoryService.create(data)  # Guardar producto si la validación es exitosa
            return jsonify(200)
        except:
            return jsonify(400)