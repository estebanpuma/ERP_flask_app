from .users import User, Role, Permission, initialize_admin_user

all_models = {
    'User': User,
    'Role': Role,
    'Permission': Permission,
    #'UserStats': UserStats,
    #'ProductionOrder': ProductionOrder,
    #'ProductionLine': ProductionLine,
    #'Sale': Sale,
    #'Customer': Customer,
    #'Product': Product,
    #'Inventory': Inventory
}