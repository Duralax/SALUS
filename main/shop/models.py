from django.db import models
from django.db.models import  CASCADE
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название товара')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание и спецификация')
    price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], max_digits=10, decimal_places=2, verbose_name='Цена')
    opt_price = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], max_digits=10, decimal_places=2, verbose_name='Оптовая цена',  blank=True, null=True)
    opt_price_if = models.PositiveIntegerField(default=10000, verbose_name='Количество, необходимое для оптовой цены', blank=True, null=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, null=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id])


