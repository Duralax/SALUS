from authentication.models import CustomUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from shop.models import Product



class Status(models.Model):
    ORD_STATUS = [
        (1, 'В обработке'),
        (2, 'Сборка'),
        (3, 'Заказ готов'),
        (4, 'Заказ завершен'),
    ]
    status = models.PositiveSmallIntegerField(("status"), choices=ORD_STATUS, default=1)
    class Meta:

        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

class Order(models.Model):
    products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.ForeignKey(Status, related_name='orders', on_delete=CASCADE, verbose_name='Статус')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())