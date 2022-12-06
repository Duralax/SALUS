

from .models import Product, Category
from django import forms
from django.forms import ModelForm, TextInput, ImageField, DecimalField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
