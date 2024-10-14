# Generated by Django 4.2 on 2024-10-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0005_hotelpagestatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelpagestatic',
            name='page_content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotelpagestatic',
            name='page_content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotelpagestatic',
            name='page_title_en',
            field=models.CharField(default='Отели Узбекистана', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotelpagestatic',
            name='page_title_ru',
            field=models.CharField(default='Отели Узбекистана', max_length=100, null=True),
        ),
    ]