from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [

    path('products/', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),





    #path('<int:id>/update', views.ProductUpdateView.as_view(), name='product_update')
]
