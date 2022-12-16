from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('orders/', views.my_orders, name='orders_user'),
    path('<int:pk>/status_update/', views.OrderChangeView.as_view(), name='status_update'),

]