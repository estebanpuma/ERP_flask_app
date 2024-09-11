from flask_restful import Resource, reqparse

from app.models import Product

from flask import jsonify, flash, json, request

from app.products.services import ProductService

from app.schemas.product import ProductSchema

from app.products.forms import ProductForm


class ProductResource(Resource):
    def get(self, product_id=None):
        print('**************ingresa a product resource**********')
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
            ProductService.create_product(data)  # Guardar producto si la validación es exitosa
            return jsonify(200)
        except:
            return jsonify(400)
