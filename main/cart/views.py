
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
@login_required(login_url='http://127.0.0.1:8000/authentication/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['quantity'] >= product.opt_price_if:
            product.price = product.opt_price
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart')

@login_required(login_url='http://127.0.0.1:8000/authentication/login/')
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cart')

@login_required(login_url='http://127.0.0.1:8000/authentication/login/')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})

@login_required(login_url='http://127.0.0.1:8000/authentication/login/')
def cart_plus_product(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.product_plus(product)
    return redirect('cart:cart')

@login_required(login_url='http://127.0.0.1:8000/authentication/login/')
def cart_minus_product(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.product_minus(product)
    return redirect('cart:cart')

