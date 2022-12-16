from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'delivery', 'phone']


class OrderChangeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        