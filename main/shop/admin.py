from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'price', 'created', 'uploaded', 'category']
    list_filter = [ 'created', 'uploaded', 'category']
    list_editable = ['price', 'category']

