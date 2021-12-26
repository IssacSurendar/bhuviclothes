from django.contrib import admin
from apps.store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'category', 'modified_date']
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)