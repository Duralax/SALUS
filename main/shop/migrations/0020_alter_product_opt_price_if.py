# Generated by Django 4.1.2 on 2022-12-06 14:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_product_opt_price_if'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='opt_price_if',
            field=models.FloatField(blank=True, default=10000, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Количество, необходимое для оптовой цены'),
        ),
    ]