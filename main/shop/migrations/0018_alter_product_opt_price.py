# Generated by Django 4.1.2 on 2022-12-06 13:33

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_product_opt_price_product_opt_price_if_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='opt_price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Оптовая цена'),
        ),
    ]
