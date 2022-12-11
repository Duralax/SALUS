
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView, UpdateView, ListView
from transliterate import slugify, translit
from . import forms
from .forms import ProductForm, CategoryForm

from .models import Category, Product
from cart.forms import CartAddProductForm

from main import settings


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
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


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


def category_create(request):
    if request.method == 'POST':

        form = CategoryForm(request.POST)
        if form.is_valid():
            slug = translit(form['name'].value(), language_code='ru', reversed=True)
            temp_slug = slug.split()
            slug = '-'.join(temp_slug)
            form.instance.slug = slug
            form.save()
            return redirect('myshop:product_list')

        else:

            form = forms.CategoryForm()

    form = CategoryForm()
    redirect('myshop:product_list')
    return render(request, 'product/category_create.html', {'form': form})

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'product/category_update.html'
    form_class = CategoryForm
    def slug_to_name(self):
        slug = translit(self.name, language_code='ru', reversed=True)
        temp_slug = slug.split()
        slug = '-'.join(temp_slug)



class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/category_delete.html'
    success_url = '/product/products'



class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = '/product/products'
    def delete_cart(self):
        from main.cart import cart
        cart.clear

class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
