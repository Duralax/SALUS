from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView

from .models import Order
from .forms import OrderCreateForm, OrderChangeForm
from cart.cart import Cart
from .models import Product
from . import models

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                order = form.save()
                this_order = Order.objects.get(id = order.pk)
                price = 0
                quantity = ''
                count = 0

                for item in cart:
                    product_in_cart = item.get('product')
                    product = Product.objects.filter(id = product_in_cart.pk)[0]
                    this_order.products.add(product)
                    price += item.get('price') * item.get('quantity')
                    if count == 0:
                        quantity += str(product.pk) + ':' + str(item.get('quantity'))
                    else:
                        quantity += ' ' + str(product.pk) + ':' + str(item.get('quantity'))
                    count += 1
                this_order.price = int(price) #при изменении в бд убрать инт
                this_order.quantity = quantity
                this_order.save()

                # очистка корзины
                cart.clear()
                return render(request, 'order_created.html',
                              {'order': order})

    else:
        form = OrderCreateForm
    return render(request, 'order.html',
                  {'cart': cart, 'form': form})


def my_orders(request):
    if request.user.role == 2:
        myorders = Order.objects.filter(user=request.user)
    else:
        myorders = Order.objects.all()
    orders = []
    for order in myorders:
        quantity = order.quantity
        str_quantites = quantity.split(' ')
        products = []
        for i in range(order.products.count()):
            for j in range(len(str_quantites)):
                temp = str_quantites[j].split(':')
                if int(temp[0]) == order.products.all()[i].pk:
                    products.append([order.products.all()[i], temp[1]])
        orders.append([[order.pk, order.user, order.address, order.price, order.status, order.delivery, order.phone, order.email, order.created, order.updated], products])
    return render(request, 'user_orders.html', {'orders': orders,})


class OrderChangeView(UpdateView):
    model = Order
    template_name = 'user_orders_status.html'
    form_class = OrderChangeForm

    def get_success_url(self):
        return reverse('orders:orders_user')






