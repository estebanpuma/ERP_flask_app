from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from .base import BaseModel, db, ValidationError

import os

from app.models.sales import SaleOrder


#Modelo Base Usuario
class User(UserMixin, BaseModel):

    __tablename__ = 'users'

    __mapper_args__ = {'polymorphic_on': 'user_type', 
                       'polymorphic_identity': 'user'
                       }

    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    last_login = db.Column(db.DateTime)
    birthday = db.Column(db.Date, nullable=True)
    description = db.Column(db.Text, nullable=True)
    user_type = db.Column(db.String(50)) 
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', back_populates='users')
    permissions = db.relationship('Permission', secondary='user_permissions', back_populates='users')

    def __repr__(self):
        return f'<Usuario: {self.username,}, cargo: {self.has_role}>'

    def validate(self):
        if not self.username or len(self.username) < 3:
            raise ValidationError("Username must be at least 3 characters long")
        
        # Aquí agregar más validaciones específicas
        return True
    

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

    def has_permission(self, permission_name):
        return any(permission.name == permission_name 
                   for role in self.roles 
                   for permission in role.permissions)

class Salesperson(User):

    __tablename__ = 'salespersons'

    __mapper_args__ = {'polymorphic_identity': 'salesperson'}

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    sales_orders_count = db.Column(db.Integer, default=0)
    visits = db.Column(db.Integer, default=0)

    sales_orders = db.relationship('SaleOrder', back_populates='salesperson', lazy=True)


class Manager(User):
    __tablename__ = 'managers'

    __mapper_args__ = {
        'polymorphic_identity': 'manager'
    }

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    

class Role(BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    users = db.relationship('User', back_populates='role')
    #permissions = db.relationship('Permission', secondary='role_permissions', back_populates='roles') #permisos al ususario no al rol


class Permission(BaseModel):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    #roles = db.relationship('Role', secondary='role_permissions', back_populates='permissions') #permisos al ususario no al rol
    users = db.relationship('User', secondary='user_permissions', back_populates='permissions')

# Tabla de asociación entre roles y permisos
user_permissions = db.Table('user_permissions',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
)


def initialize_admin_user():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        username = os.environ.get('ADMIN_USER_NAME')
        email = os.environ.get('ADMIN_USER_EMAIL')
        password = os.environ.get('ADMIN_USER_PASSWORD')
        ci = '0000000000'
        
        if not password:
            raise ValueError("Admin password not set in environment variables")

        adminuser = User(id=1, ci=ci, username=username, email=email)
        adminuser.set_password(password)
        
        print(adminuser.username, adminuser.password, adminuser.email)
        # Crear roles y permisos básicos si no existen
        admin_role = Role.query.filter_by(name='admin').first()
        if not admin_role:
            admin_role = Role(id= 1, name='admin', description='Administrator')
            admin_role.save()

        # Asignar rol de admin al superusuario
        adminuser.roles = [admin_role]

        if adminuser.save():
            print(f"Admin {username} created successfully")
        else:
            print("Failed to create admin")
    else:
        print("Superuser already admin")