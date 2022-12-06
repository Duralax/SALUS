# Generated by Django 4.1.2 on 2022-12-06 13:32

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='opt_price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AddField(
            model_name='product',
            name='opt_price_if',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]