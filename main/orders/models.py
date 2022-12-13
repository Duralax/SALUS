from authentication.models import CustomUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from shop.models import Product


class Order(models.Model):
    ORD_STATUS = [
        ('Обработка заказа', 'В обработке'),
        ('Сборка заказа', 'Сборка'),
        ('Заказ готов', 'Заказ готов'),
        ('Заказ завершен', 'Заказ завершен'),
    ]

    products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField( verbose_name='Общая цена', null=True)
    email = models.EmailField()
    quantity = models.CharField(max_length= 100, verbose_name='Количество', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING, null=True)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(("status"), choices=ORD_STATUS, default='Обработка заказа', max_length=17)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())