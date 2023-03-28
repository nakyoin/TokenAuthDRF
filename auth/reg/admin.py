from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ProductManager)
admin.site.register(Order)
admin.site.register(CountryProd)
admin.site.register(Cart)