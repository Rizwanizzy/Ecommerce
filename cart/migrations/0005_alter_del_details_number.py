# Generated by Django 4.1.2 on 2022-12-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_del_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='del_details',
            name='number',
            field=models.IntegerField(),
        ),
    ]