# Generated by Django 5.0.4 on 2024-04-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_alter_addontourwithprice_descr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourwithprice',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='Сделать популярным ?'),
        ),
    ]
