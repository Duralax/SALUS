from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Product



def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:

                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         user=request.user)
            # очистка корзины
            cart.clear()
            return render(request, 'order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'order.html',
                  {'cart': cart, 'form': form})


def orders(request):
    orders = OrderItem.objects.all()
    user_orders = []
    for order in orders:
        if order.user == request.user:
            user_orders.append(order)
    context = {'orders': user_orders}
    return render(request, 'user_orders.html', context)


