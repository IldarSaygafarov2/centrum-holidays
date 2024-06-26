# Generated by Django 5.0.4 on 2024-04-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_tour_full_description_tour_full_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст отзыва'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст отзыва'),
        ),
    ]
