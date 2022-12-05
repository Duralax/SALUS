
from django.http import HttpRequest
from django.shortcuts import render
from .models import Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Product
from . import models

def order_create(request):
    cart = Cart(request)


    if request.method == 'POST':
        try:
            object = models.Order.objects.get(user_id=request.user.pk)
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()

                for item in cart:

                    Order.objects.create(product=item,
                                             price=item['price'],
                                             quantity=item['quantity'],
                                             user=request.user)

                # очистка корзины
                cart.clear()
                return render(request, 'order_created.html',
                              {'order': order})
        except:
            return render(request, 'order.html',
                          {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm
    return render(request, 'order.html',
                  {'cart': cart, 'form': form})

#def orders(request):
    #orders = Order.objects.all()
    #order_items = OrderItem.objects.all()
    #user_order_items = []
   # for order in order_items:
    #    if order.user == request.user:
#
 #           user_order_items.append(order)
  #  context = {'order_items': user_order_items}
   # return render(request, 'user_orders.html', context)


def my_orders(request):
    products = Product.objects.all()
    myorders = Order.objects.filter(user_id=request.user)
    product_ordered = OrderItem.objects.all()
    assert isinstance(request, HttpRequest)
    return render(request, 'user_orders.html', {'products': products, 'product_ordered': product_ordered, 'myorders': myorders, })


