# Generated by Django 4.2 on 2024-10-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_tourwithprice_season_en_tourwithprice_season_ru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourwithprice',
            name='stars',
            field=models.CharField(blank=True, default='0', max_length=100, null=True, verbose_name='Звездность'),
        ),
    ]