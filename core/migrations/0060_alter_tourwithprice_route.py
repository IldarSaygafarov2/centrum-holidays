# Generated by Django 4.2 on 2024-10-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_tourwithprice_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourwithprice',
            name='route',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка маршрута тура'),
        ),
    ]
