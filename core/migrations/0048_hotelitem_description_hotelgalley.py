# Generated by Django 4.2 on 2024-04-27 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_bun'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelitem',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='HotelGalley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='hotels/', verbose_name='Фото')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hotelitem', verbose_name='ОТЕЛЬ')),
            ],
        ),
    ]
