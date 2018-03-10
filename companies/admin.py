from django.contrib import admin

# Register your models here.
from .models import Subcategory,Sku,Subcategory_SKU

admin.site.register(Subcategory)
admin.site.register(Sku)
admin.site.register(Subcategory_SKU)

