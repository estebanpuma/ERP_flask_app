from .users import User, Role, Permission, Salesperson, initialize_admin_user
from .crm import Client, ClientCategory, Contact
from .inventory import Product, ProductCategory, Color, Size, SizeSeries, ProductSubCategory, Stock
from .sales import SaleOrder, SaleOrderProduct, ProductPriceHistory
from .payment import PaymentMethod, PaymentPlan, Installment

all_models = {
    'User': User,
    'Role': Role,
    'Permission': Permission,
    'Client': Client,
    'ClientCategory': ClientCategory,
    'Contact': Contact,
    #'UserStats': UserStats,
    #'ProductionOrder': ProductionOrder,
    #'ProductionLine': ProductionLine,
    #'Sale': Sale,
    'Product': Product,
    'Stock': Stock,
    'ProductCategory': ProductCategory,
    'ProductSubCategory': ProductSubCategory,
    'Size': Size,
    'SizeSeries': SizeSeries,
    'Color': Color

    #'Inventory': Inventory
}