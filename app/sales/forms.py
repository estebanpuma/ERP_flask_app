from flask_wtf import FlaskForm

from wtforms import RadioField, StringField, EmailField, SubmitField, BooleanField, SelectField, FieldList

from wtforms.validators import DataRequired, Optional, Email

from app.models import SaleOrder, SaleOrderProduct


class SaleOrderForm(FlaskForm):

    order_number = StringField('Numero', validators=[DataRequired()])

    name = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio.")])
    description = StringField('Direccion', validators=[Optional()])
    client = SelectField('Categoria', choices=[('', 'Seleccione una linea')], validators=[Optional()])
    sub_category = SelectField('Categoria', choices=[('', 'Seleccione una sublinea')], validators=[Optional()])
    submit = SubmitField('Guardar')

    #def __init__(self, *args, **kwargs):
     #   super(ProductForm, self).__init__(*args, **kwargs)
      ## self.sub_category.choices += [(c.id, c.name) for c in ProductSubCategory.query.all()]


class ProductCategoryForm(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio.")])
    description = StringField('Direccion', validators=[DataRequired()])
    submit = SubmitField('Guardar')


class ProductSubCategoryForm(FlaskForm):

    name = StringField('Nombre', validators=[DataRequired(message="Este campo es obligatorio.")])
    description = StringField('Direccion', validators=[Optional()])
    category = SelectField('Categoria', choices=[('', 'Seleccione una linea')], validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def __init__(self, *args, **kwargs):
        super(ProductSubCategoryForm, self).__init__(*args, **kwargs)
        #self.category.choices += [(c.id, c.name) for c in ProductCategory.query.all()]