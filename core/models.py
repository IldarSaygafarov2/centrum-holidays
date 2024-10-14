from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Review(models.Model):
    author = models.CharField(max_length=20, verbose_name='Имя автора')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Client(models.Model):
    img = models.ImageField(verbose_name='Фото компании клиента', upload_to='clients/')
    company_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Advantage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    icon = models.FileField(verbose_name='Иконка', upload_to='advantages', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Destination(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    short_description = models.TextField(max_length=250, verbose_name='Краткое описание')
    preview = models.ImageField(verbose_name='Заставка', upload_to='destinations')
    is_popular = models.BooleanField(verbose_name='Добавить в раздел популярные туры?', default=False)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Tour(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    preview = models.ImageField(verbose_name='Заставка', upload_to='tours/', null=True, blank=True)
    short_description = models.TextField(max_length=500, verbose_name='Краткое описание', null=True, blank=True)
    full_description = RichTextUploadingField(verbose_name='Полное описание 1', blank=True, null=True)
    map_link = models.CharField(max_length=1000, verbose_name='Ссылка на карту', blank=True, null=True)
    full_description2 = RichTextUploadingField(verbose_name='Полное описание 2', blank=True, null=True)
    is_popular = models.BooleanField(verbose_name='Популярный тур?', default=False)
    is_recommended = models.BooleanField(verbose_name='Рекомендуемый тур?', default=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name='Направление', null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class TourWithPrice(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    preview = models.ImageField(verbose_name='Заставка', upload_to='tours/', null=True, blank=True)
    full_description = RichTextUploadingField(verbose_name='Детали', null=True, blank=True)
    price = models.CharField(verbose_name='Стоимость', null=True, blank=True, max_length=20)
    days = models.PositiveSmallIntegerField(verbose_name='Дней', null=True, blank=True)
    nights = models.PositiveSmallIntegerField(verbose_name='Ночей', null=True, blank=True)
    season = models.CharField(verbose_name='Сезон', max_length=50, null=True, blank=True)
    stars = models.CharField(verbose_name='Звездность', default='0', max_length=100, null=True, blank=True)
    route = models.URLField(verbose_name='Ссылка маршрута тура', blank=True, null=True)
    is_popular = models.BooleanField(default=False, verbose_name='Сделать популярным ?')
    is_recommended = models.BooleanField(default=False, verbose_name='Сделать рекомендуемым ?')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур с ценой'
        verbose_name_plural = 'Туры с ценой'


class PriceByHumanTour(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    category_of_price = models.CharField(verbose_name='Категория для цены', max_length=100, null=True, blank=True)
    qty = models.IntegerField(verbose_name='Количество человек')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return f'{self.qty} чел - {self.price} USD'

    class Meta:
        verbose_name = 'Стоимость с человека'
        verbose_name_plural = 'Стоимость с человека'


class PlacesTourWithPrice(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    place = models.CharField(max_length=50, verbose_name='Место посещения')

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Место посещения тура'
        verbose_name_plural = 'Места посещений тура'


class DayTourWithPrice(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    name = models.CharField(verbose_name='Заголовок', max_length=100)
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День тура'
        verbose_name_plural = 'Дни тура'


class AddonTourWithPrice(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    name = models.CharField(verbose_name='Заголовок', max_length=100)
    descr = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительная экскурсия'
        verbose_name_plural = 'Дополнительные экскурсии'


class TourCondition(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Условие тура'
        verbose_name_plural = 'Условия тура'


class TourHotel(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Отель тура'
        verbose_name_plural = 'Отели тура'


class TourPriceInclude(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    text = models.TextField(verbose_name='Текст', null=True)

    class Meta:
        verbose_name = 'Цена включает'
        verbose_name_plural = 'Цена включает'


class TourPriceDoesNotInclude(models.Model):
    tour = models.ForeignKey(TourWithPrice, on_delete=models.CASCADE, verbose_name='Тур', null=True)
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Цена не включает'
        verbose_name_plural = 'Цена не включает'


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    excerpt = models.TextField(verbose_name='Краткое описание', max_length=500)
    preview = models.ImageField(verbose_name='Заставка', upload_to='articles/')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class HotelItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    slug = models.SlugField(verbose_name='Слаг')
    preview = models.ImageField(verbose_name='Фото', upload_to='hotels/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Bun(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    hotel = models.ForeignKey(HotelItem, on_delete=models.CASCADE, verbose_name='ОТЕЛЬ')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга отеля'
        verbose_name_plural = 'Услуги отеля'


class HotelGallery(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='hotels/')
    hotel = models.ForeignKey(HotelItem, on_delete=models.CASCADE, verbose_name='ОТЕЛЬ')
    
    class Meta:
        verbose_name = 'Фото отеля'
        verbose_name_plural = 'Фото отеля'