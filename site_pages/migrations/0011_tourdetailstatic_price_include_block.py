# Generated by Django 4.2 on 2024-10-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0010_infopagestatic_page_content_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetailstatic',
            name='price_include_block',
            field=models.CharField(default='Стоимость тура на весну 2025, с человека:', max_length=150),
        ),
    ]