from django.db import models


class HomePageStatic(models.Model):
    hero_title = models.CharField(verbose_name='Заголовок первой секции', max_length=100,
                                  default='Туры в Узбекистан с Canaan-travel')
    hero_subtitle = models.CharField(verbose_name='Подзаголовок первой секции', max_length=100,
                                     default='Откройте для себя сказочный Восток!')
    hero_years = models.CharField(verbose_name='Лет на рынке', max_length=100, default='17')
    hero_hotel_total = models.CharField(verbose_name='Кол-во отелей', max_length=100, default='500+')
    hero_guides_total = models.CharField(verbose_name='Кол-во гидов', max_length=100, default='300+')
    section_title_1 = models.CharField(verbose_name='Заголовок секции "Популярные направления"', max_length=100,
                                       default='Популярные направления')
    section_title_2 = models.CharField(verbose_name='Заголовок секции "Популярные туры"', max_length=100,
                                       default='Популярные туры')
    special_offer_text = models.CharField(max_length=100, default='Специальное предложение')
    special_offer_text_2 = models.CharField(max_length=100, default='Путешествуйте дешевле!')
    we_recommend_title = models.CharField(max_length=100, default='Мы рекомендуем')
    know_more_block = models.CharField(max_length=100, default='Узнайте больше о востоке')
    know_more_block_2_title = models.CharField(max_length=100, default='Узнайте о востоке больше вместе с нами')
    know_more_block_2_text = models.TextField(default='''Canaan-travel — туристическая компания полного цикла, ставящая перед собой цель открыть красоту всего мира для каждого человека сегодня. Мы стремимся ближе познакомить Восток и Запад, предлагая путешествия по Центральной Азии туристам из СНГ, Европы и Америки и поездки по всему миру жителям Центральной Азии.

Мы работаем как с отдельными туристами, так и с компаниями. Наличие собственных авиакассы, автотранспорта и сотрудничество с лучшими гидами и отелями помогают нам формировать уникальные предложения в индивидуальном порядке.''')

    advantages_title = models.CharField(max_length=100, default='Преимущества нашего обслуживания')
    email_resend_title = models.CharField(max_length=100, default='Подпишись на рассылку интересных предложений')
    booking_block_title = models.CharField(max_length=100, default='Хотите забронировать тур?')
    booking_block_text = models.CharField(max_length=150,
                                          default='Заполните небольшую форму и мы подберем тур именно для вас')
    our_partners_title = models.CharField(max_length=150, default='Наши партнеры')
    footer_text = models.TextField(default='''Информация туристам Туры в Узбекистан Достопримечательности.
Наша компания имеет все необходимые лицензии и сертификаты качества.

Независимые отзывы о нас читайте на TripAdvisor''')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class OurMissionStatic(models.Model):
    page_title = models.CharField(max_length=100, default='Наша миссия')
    page_content = models.TextField()

    class Meta:
        verbose_name = 'Наша миссия'
        verbose_name_plural = 'Наша миссия'
