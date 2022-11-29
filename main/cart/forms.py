from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value= 1, label='Количество', widget= forms.NumberInput(attrs={'class': 'inpt_class'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)