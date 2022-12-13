# Generated by Django 4.1.2 on 2022-12-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_status_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Общая цена'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=100, null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Обработка заказа', 'В обработке'), ('Сборка заказа', 'Сборка'), ('Заказ готов', 'Заказ готов'), ('Заказ завершен', 'Заказ завершен'), ('Заказ отменен', 'Заказ отменен')], default='Обработка заказа', max_length=17, verbose_name='status'),
        ),
    ]