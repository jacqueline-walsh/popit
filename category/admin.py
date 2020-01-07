from django.contrib import admin
from category.models import Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
