# Generated by Django 4.1.2 on 2023-01-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_orders_product_ordered_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='price',
        ),
        migrations.AddField(
            model_name='ordered_items',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]