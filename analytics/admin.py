from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Vendor)
admin.site.register(ProductType)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(InventoryProduct)
admin.site.register(Order)