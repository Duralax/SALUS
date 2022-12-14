# Generated by Django 4.1.2 on 2022-12-09 12:26

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_product_opt_price_if'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.001'))], verbose_name='Цена'),
        ),
    ]
