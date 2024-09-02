from .users import User, Role, Permission, initialize_admin_user
from .crm import Client, ClientCategory, Contact

all_models = {
    'User': User,
    'Role': Role,
    'Permission': Permission,
    'Client': Client,
    'ClientCategory': ClientCategory,
    'Contact': Contact
    #'UserStats': UserStats,
    #'ProductionOrder': ProductionOrder,
    #'ProductionLine': ProductionLine,
    #'Sale': Sale,
    #'Product': Product,
    #'Inventory': Inventory
}