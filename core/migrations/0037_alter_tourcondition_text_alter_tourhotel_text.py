# Generated by Django 5.0.4 on 2024-04-16 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_tourpricedoesnotinclude_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourcondition',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='tourhotel',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
