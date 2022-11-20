from .models import Product
from django import forms
from .models import Image
from django.forms import ModelForm, TextInput, ImageField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'







class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
