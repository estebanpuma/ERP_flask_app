from app import ma

from marshmallow import fields, validate

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.models import Product, ProductCategory, ProductSubCategory


class ProductCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductCategory
        load_instance = True

class ProductSubCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductSubCategory
        include_fk = True
        load_instance = True

    #category = fields.Nested(ProductCategorySchema)

class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True
        load_instance = True

    category = fields.Nested(ProductCategorySchema)
    sub_category = fields.Nested(ProductSubCategorySchema)


#******Validar formulario*************
class ProductInputSchema(ma.Schema):
    code = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    description = fields.Str()
    category_id = fields.Int(required=True)
    sub_category_id = fields.Int(required=True)