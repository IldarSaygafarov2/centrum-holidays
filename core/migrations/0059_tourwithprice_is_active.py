# Generated by Django 4.2 on 2024-10-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_alter_tourwithprice_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourwithprice',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Показать/скрыть тур'),
        ),
    ]