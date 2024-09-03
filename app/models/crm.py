from flask_login import UserMixin

from .base import BaseModel, db, ValidationError

import os


# Modelo para clasificar los clientes según su sector: Gubernamental, Corporativo, Educativo, ONG, etc.
class ClientCategory(BaseModel):

    __tablename__ = 'client_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # Ejemplo: 'Gubernamental', 'Corporativo', 'Educativo'
    description = db.Column(db.String(200), nullable=True)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Categoria_cliente(nombre={self.name})>'


#Modelo clientes
class Client(BaseModel):
    
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(120), nullable=True, unique=False)
    phone = db.Column(db.String(20), nullable=True)
    ruc_or_ci = db.Column(db.String(13), nullable=True, unique=True)  # Puede ser cédula o RUC
    

    client_type = db.Column(db.String(100), nullable=False)

    client_category_id = db.Column(db.Integer, db.ForeignKey('client_categories.id', ondelete='RESTRICT'), nullable=True)

    client_category = db.relationship('ClientCategory', backref='clients')
    contacts = db.relationship('Contact', back_populates='client', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Cliente(nombre={self.name}, ruc_o_cedula={self.ruc_or_ci})>'


class Contact(BaseModel):

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    position = db.Column(db.String(100), nullable=True)  # Cargo del contacto
    notes = db.Column(db.String, nullable=True)
    birth_date = db.Column(db.String(10), nullable=True) 
    # Relación con Client
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Client', back_populates='contacts')

    def __repr__(self):
        return f'<Contacto(nombre={self.name}, client={self.client.name})>'
    
    