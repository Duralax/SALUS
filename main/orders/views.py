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
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                order = form.save()
                this_order = Order.objects.get(id = order.pk)
                price = 0
                quantity = ''
                count = 0
                for item in cart:
                    product_in_cart =  item.get('product')
                    product = Product.objects.filter(id = product_in_cart.pk)[0]
                    this_order.products.add(product)
                    price += item.get('price') * item.get('quantity')
                    if count == 0:
                        quantity += str(item.get('quantity'))
                    else:
                        quantity += ' ' + str(item.get('quantity'))
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
    myorders = Order.objects.filter(user=request.user)
    for order in myorders:
        quantity = order.quantity
        #print('===================', quantity)
        quantites = quantity.split(' ')
        products = []
        count_products = len(order.products)
        for i in range(count_products):
            products.append([order.products[i], quantites[i]])

    print('===================', products)
    #assert isinstance(request, HttpRequest)
    #return render(request, 'user_orders.html', {'products': products,  'myorders': myorders, })






