from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myshop'

urlpatterns = [

    path('products/', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='product_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    #path('<int:id>/update', views.ProductUpdateView.as_view(), name='product_update')

