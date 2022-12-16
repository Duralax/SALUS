# Generated by Django 4.1.2 on 2022-12-16 12:32

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='opt_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Оптовая цена'),
        ),
    ]
