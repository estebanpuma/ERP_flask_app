from .base import BaseModel, db

# Tabla intermedia entre Product y Color
product_color_association = db.Table('product_color_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('color_id', db.Integer, db.ForeignKey('colors.id'), primary_key=True)
)

# Tabla intermedia entre Product y Size
product_size_association = db.Table('product_size_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
    db.Column('size_id', db.Integer, db.ForeignKey('sizes.id'), primary_key=True)
)

class ProductCategory(BaseModel):
    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    products = db.relationship('Product', back_populates='category', cascade='all, delete-orphan')
    sub_categories = db.relationship('ProductSubCategory', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<ProductCategory(name={self.name})>'
    

class ProductSubCategory(BaseModel):
    __tablename__ = 'product_sub_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id', ondelete='Cascade'), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    category = db.relationship('ProductCategory', back_populates='sub_categories')
    products = db.relationship('Product', back_populates='sub_category', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<ProductCategory(name={self.name})>'


class Product(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False, unique=True)  # Código único del modelo
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
   
    
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'), nullable=False)
    sub_category_id = db.Column(db.Integer, db.ForeignKey('product_sub_categories.id'), nullable=False)

    is_deleted = db.Column(db.Boolean, default=False)

    category = db.relationship('ProductCategory', back_populates='products')
    sub_category = db.relationship('ProductSubCategory', back_populates='products')

    colors = db.relationship('Color', secondary=product_color_association, back_populates='products')
    sizes = db.relationship('Size', secondary=product_size_association, back_populates='products')

    stock = db.relationship('Stock', back_populates='product')

    material_details = db.relationship('ProductMaterialDetail', back_populates='product', cascade="all, delete-orphan")

    sale_order = db.relationship('SaleOrderProduct', back_populates='products')
    price_history = db.relationship('ProductPriceHistory', back_populates='product')

    def __repr__(self):
        return f'<Product(code={self.code}, name={self.name})>'
    

class Material(BaseModel):
    __tablename__ = 'materials'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False, unique=True)  # Ejemplo: 'Cuero', 'Textil', 'Sintético'

    description = db.Column(db.String(), nullable=True)

    product_material_details = db.relationship('ProductMaterialDetail', back_populates='material')

    def __repr__(self):
        return f'<Material(name={self.name})>'
    

class ProductMaterialDetail(BaseModel):
    __tablename__ = 'product_material_details'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False, default=1.0)

    product = db.relationship('Product', back_populates='material_details')
    material = db.relationship('Material', back_populates='product_material_details')

    def __repr__(self):
        return f'<ProductMaterialDetail(product={self.product.name}, material={self.material.name}, quantity={self.quantity})>'


class Stock(BaseModel):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product = db.relationship('Product', back_populates='stock')

    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'), nullable=False)
    size = db.relationship('Size')

    color_id = db.Column(db.Integer, db.ForeignKey('colors.id'), nullable=False)
    color = db.relationship('Color')

    quantity = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'<Stock(product={self.product.name}, size={self.size.value}, color={self.color.name}, quantity={self.quantity})>'


class Color(BaseModel):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # Ejemplo: 'Rojo', 'Azul', 'Negro'
    hex_value = db.Column(db.String(7), nullable=True)  # Ejemplo: '#FF5733'
    
    products = db.relationship('Product', secondary=product_color_association, back_populates='colors')

    def __repr__(self):
        return f'<Color(name={self.name})>'
    




class SizeSeries(BaseModel):
    __tablename__ = 'size_series'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # Ejemplo: 'Serie 1', 'Serie 2'
    description = db.Column(db.String(200), nullable=True)

    sizes = db.relationship('Size', back_populates='series')

    def __repr__(self):
        return f'<SizeSeries(name={self.name})>'


class Size(BaseModel):
    __tablename__ = 'sizes'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10), nullable=False, unique=True)  # Ejemplo: '40', 'M', '10'
    
    series_id = db.Column(db.Integer, db.ForeignKey('size_series.id'), nullable=False)
    series = db.relationship('SizeSeries', back_populates='sizes')

    products = db.relationship('Product', secondary=product_size_association, back_populates='sizes')

    def __repr__(self):
        return f'<Size(value={self.value}, series={self.series.name})>'



