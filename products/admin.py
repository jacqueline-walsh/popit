from django.contrib import admin
from products.models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    list_filter = ('category',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'category')
    list_editable = ['price', 'stock']

admin.site.register(Product, ProductAdmin)
