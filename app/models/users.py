from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from .base import BaseModel, db, ValidationError

import os



# Tabla de asociación entre usuarios y roles
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
)

#Modelo Usuario
class User(UserMixin, BaseModel):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String, unique=True, nullable=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    last_login = db.Column(db.DateTime)
    birthday = db.Column(db.Date, nullable=True)
    description = db.Column(db.Text, nullable=True)
    roles = db.relationship('Role', secondary=user_roles, back_populates='users')

    def __repr__(self):
        return f'<Usuario: {self.username,}, cargo: {self.has_role}>'

    def validate(self):
        if not self.username or len(self.username) < 3:
            raise ValidationError("Username must be at least 3 characters long")
        
        if not self.email:
            raise ValidationError("Invalid email format")
        
        if not self.password:
            raise ValidationError("Password is required")
        
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


class Role(BaseModel):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    users = db.relationship('User', secondary=user_roles, back_populates='roles')
    permissions = db.relationship('Permission', secondary='role_permissions', back_populates='roles')


class Permission(BaseModel):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.String(255))
    roles = db.relationship('Role', secondary='role_permissions', back_populates='permissions')

# Tabla de asociación entre roles y permisos
role_permissions = db.Table('role_permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True),
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