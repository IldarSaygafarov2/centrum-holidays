# Generated by Django 4.2 on 2024-10-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagestatic',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='advantages_title_en',
            field=models.CharField(default='Преимущества нашего обслуживания', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='advantages_title_ru',
            field=models.CharField(default='Преимущества нашего обслуживания', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='booking_block_text_en',
            field=models.CharField(default='Заполните небольшую форму и мы подберем тур именно для вас', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='booking_block_text_ru',
            field=models.CharField(default='Заполните небольшую форму и мы подберем тур именно для вас', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='booking_block_title_en',
            field=models.CharField(default='Хотите забронировать тур?', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='booking_block_title_ru',
            field=models.CharField(default='Хотите забронировать тур?', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='email_resend_title_en',
            field=models.CharField(default='Подпишись на рассылку интересных предложений', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='email_resend_title_ru',
            field=models.CharField(default='Подпишись на рассылку интересных предложений', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='footer_text_en',
            field=models.TextField(default='Информация туристам Туры в Узбекистан Достопримечательности.\nНаша компания имеет все необходимые лицензии и сертификаты качества.\n\nНезависимые отзывы о нас читайте на TripAdvisor', null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='footer_text_ru',
            field=models.TextField(default='Информация туристам Туры в Узбекистан Достопримечательности.\nНаша компания имеет все необходимые лицензии и сертификаты качества.\n\nНезависимые отзывы о нас читайте на TripAdvisor', null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_guides_total_en',
            field=models.CharField(default='300+', max_length=100, null=True, verbose_name='Кол-во гидов'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_guides_total_ru',
            field=models.CharField(default='300+', max_length=100, null=True, verbose_name='Кол-во гидов'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_hotel_total_en',
            field=models.CharField(default='500+', max_length=100, null=True, verbose_name='Кол-во отелей'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_hotel_total_ru',
            field=models.CharField(default='500+', max_length=100, null=True, verbose_name='Кол-во отелей'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_subtitle_en',
            field=models.CharField(default='Откройте для себя сказочный Восток!', max_length=100, null=True, verbose_name='Подзаголовок первой секции'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_subtitle_ru',
            field=models.CharField(default='Откройте для себя сказочный Восток!', max_length=100, null=True, verbose_name='Подзаголовок первой секции'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_title_en',
            field=models.CharField(default='Туры в Узбекистан с Canaan-travel', max_length=100, null=True, verbose_name='Заголовок первой секции'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_title_ru',
            field=models.CharField(default='Туры в Узбекистан с Canaan-travel', max_length=100, null=True, verbose_name='Заголовок первой секции'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_years_en',
            field=models.CharField(default='17', max_length=100, null=True, verbose_name='Лет на рынке'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='hero_years_ru',
            field=models.CharField(default='17', max_length=100, null=True, verbose_name='Лет на рынке'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_2_text_en',
            field=models.TextField(default='Canaan-travel — туристическая компания полного цикла, ставящая перед собой цель открыть красоту всего мира для каждого человека сегодня. Мы стремимся ближе познакомить Восток и Запад, предлагая путешествия по Центральной Азии туристам из СНГ, Европы и Америки и поездки по всему миру жителям Центральной Азии.\n\nМы работаем как с отдельными туристами, так и с компаниями. Наличие собственных авиакассы, автотранспорта и сотрудничество с лучшими гидами и отелями помогают нам формировать уникальные предложения в индивидуальном порядке.', null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_2_text_ru',
            field=models.TextField(default='Canaan-travel — туристическая компания полного цикла, ставящая перед собой цель открыть красоту всего мира для каждого человека сегодня. Мы стремимся ближе познакомить Восток и Запад, предлагая путешествия по Центральной Азии туристам из СНГ, Европы и Америки и поездки по всему миру жителям Центральной Азии.\n\nМы работаем как с отдельными туристами, так и с компаниями. Наличие собственных авиакассы, автотранспорта и сотрудничество с лучшими гидами и отелями помогают нам формировать уникальные предложения в индивидуальном порядке.', null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_2_title_en',
            field=models.CharField(default='Узнайте о востоке больше вместе с нами', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_2_title_ru',
            field=models.CharField(default='Узнайте о востоке больше вместе с нами', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_en',
            field=models.CharField(default='Узнайте больше о востоке', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='know_more_block_ru',
            field=models.CharField(default='Узнайте больше о востоке', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='our_partners_title_en',
            field=models.CharField(default='Наши партнеры', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='our_partners_title_ru',
            field=models.CharField(default='Наши партнеры', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='section_title_1_en',
            field=models.CharField(default='Популярные направления', max_length=100, null=True, verbose_name='Заголовок секции "Популярные направления"'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='section_title_1_ru',
            field=models.CharField(default='Популярные направления', max_length=100, null=True, verbose_name='Заголовок секции "Популярные направления"'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='section_title_2_en',
            field=models.CharField(default='Популярные туры', max_length=100, null=True, verbose_name='Заголовок секции "Популярные туры"'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='section_title_2_ru',
            field=models.CharField(default='Популярные туры', max_length=100, null=True, verbose_name='Заголовок секции "Популярные туры"'),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='special_offer_text_2_en',
            field=models.CharField(default='Путешествуйте дешевле!', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='special_offer_text_2_ru',
            field=models.CharField(default='Путешествуйте дешевле!', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='special_offer_text_en',
            field=models.CharField(default='Специальное предложение', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='special_offer_text_ru',
            field=models.CharField(default='Специальное предложение', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='we_recommend_title_en',
            field=models.CharField(default='Мы рекомендуем', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepagestatic',
            name='we_recommend_title_ru',
            field=models.CharField(default='Мы рекомендуем', max_length=100, null=True),
        ),
    ]
