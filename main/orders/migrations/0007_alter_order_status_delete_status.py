# Generated by Django 4.1.2 on 2022-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_status_order_user_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'В обработке'), (2, 'Сборка'), (3, 'Заказ готов'), (4, 'Заказ завершен')], default=1, verbose_name='status'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
