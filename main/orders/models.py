from authentication.models import CustomUser
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from shop.models import Product


class Order(models.Model):
    ORD_STATUS = [
        ('Обработка заказа', 'В обработке'),
        ('Сборка заказа', 'Сборка'),
        ('Заказ готов', 'Заказ готов'),
        ('Заказ завершен', 'Заказ завершен'),
        ('Заказ отменен', 'Заказ отменен'),
        ('Заказ возвращен', 'Заказ возвращен')
    ]

    DELIVERY = [
        ('Самовывоз', 'Самовывоз' ),
        ('Доставка', 'Доставка')

    ]

    products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField( verbose_name='Общая цена', null=True)
    email = models.EmailField()
    quantity = models.CharField(max_length= 100, verbose_name='Количество', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING, null=True)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery = models.CharField(("delivery"), choices=DELIVERY, default='Самовывоз', max_length=17)
    status = models.CharField(("status"), choices=ORD_STATUS, default='Обработка заказа', max_length=17)
    phone = PhoneNumberField(verbose_name='Контактный телефон', null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())