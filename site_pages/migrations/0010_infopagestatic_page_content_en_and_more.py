# Generated by Django 4.2 on 2024-10-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0009_infopagestatic'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopagestatic',
            name='page_content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infopagestatic',
            name='page_content_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='infopagestatic',
            name='page_title_en',
            field=models.CharField(default='Виза - информация туристам', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infopagestatic',
            name='page_title_ru',
            field=models.CharField(default='Виза - информация туристам', max_length=100, null=True),
        ),
    ]
