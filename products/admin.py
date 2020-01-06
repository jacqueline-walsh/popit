from django.contrib import admin
from products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    list_display_links = ('id', 'name')
    list_editable = ['price', 'stock']

    admin.site.register(Product)
