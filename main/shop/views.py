from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView, UpdateView
from .forms import ProductForm
from .models import Category, Product
from . import forms


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'product/product_create.html', {'form': form, 'img_obj': img_obj})

        else:

            form = forms.ProductForm()

    form = ProductForm()

    return render(request, 'product/product_create.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_create.html'
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product

    template_name = 'product/product_delete.html'
    success_url = '/product/products'
