import os

import requests
from django.conf import settings
from django.core import mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from . import models


# Create your views here.


def book_tour_with_price(request):
    data = request.POST
    msg = f"""
Имя пользователя: {data['username']}
Почта: {data['email']}
Сообщение: {data['text']}
"""
    mail.send_mail(
        subject='Бронирование тура',
        message=msg,
        from_email=data["email"],
        recipient_list=['travelcanaanbooking@gmail.com'],
    )
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    return redirect('home')


def book_hotel(request):
    data = request.POST
    msg = f"""
Имя пользователя: {data['username']}
Почта: {data['email']}
Сообщение: {data['text']}
"""
    mail.send_mail(
        subject='Бронирование отеля',
        message=msg,
        from_email=data["email"],
        recipient_list=['travelcanaanbooking@gmail.com'],
    )
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    return redirect('home')

def send_mail(request):
    data = request.POST
    msg = f'Почта отправленная с сайта: {data["email"]}'
    mail.send_mail(
        subject='Оставленная почта',
        message=f'Оставленная почта с сайта: {data["email"]}',
        from_email=data["email"],
        recipient_list=['travelcanaanbooking@gmail.com'],
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD
    )
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))

    return redirect('home')


def send_username_and_phone(request):
    data = request.POST

    msg = f"Имя пользователя: {data['username']}\nНомер телефона: {data['phone']}"
    mail.send_mail(
        subject='Данные пользователя для бронирования тура',
        message=f"Имя пользователя: {data['username']}\nНомер телефона: {data['phone']}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['travelcanaanbooking@gmail.com'],
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD
    )
    requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    return redirect('home')


def book_tour(request):
    data = request.POST

    msg = f"""
***Бронирование тура***
Имя: {data['username']}
Дата: {data['date']}
Почта: {data['email']}
Номер телефона: {data['phone']}
Комментарий: {data['body']}
"""
    mail.send_mail(
        subject='Бронирование тура',
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['travelcanaanbooking@gmail.com'],
        auth_user=settings.EMAIL_HOST_USER,
        auth_password=settings.EMAIL_HOST_PASSWORD
    )
    resp = requests.post(settings.CHANNEL_API_LINK.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_ID,
        text=msg
    ))
    resp.raise_for_status()
    print(resp)
    with open(os.path.join(settings.BASE_DIR, 'resp.txt'), mode='w', encoding='utf-8') as f:
        f.write(resp.text)
    return redirect('home')


def home_view(request):
    reviews = models.Review.objects.all()
    clients = models.Client.objects.all()
    advantages = models.Advantage.objects.all()
    destinations = models.Destination.objects.filter(is_popular=True)

    popular_tours = models.TourWithPrice.objects.filter(is_popular=True)
    recommended_tours = models.TourWithPrice.objects.filter(is_recommended=True)

    articles = models.Article.objects.all()

    context = {
        'reviews': reviews,
        'clients': clients,
        'advantages': advantages,
        'destinations': destinations,
        'popular_tours': popular_tours,
        'recommended_tours': recommended_tours,
        'articles': articles
    }
    return render(request, 'core/index.html', context)


def about_view(request):
    clients = models.Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'core/about.html', context)


def reviews_view(request):
    reviews = models.Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'core/reviews.html', context)


def booking_view(request):
    return render(request, 'core/booking.html')


def mission_view(request):
    return render(request, 'core/mission.html')


def tourists_info_view(request):
    return render(request, 'core/info.html')


def blog_view(request):
    articles = models.Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'core/blog.html', context)


def destinations_view(request, slug):
    destination = models.Destination.objects.get(slug=slug)
    tours = models.Tour.objects.filter(destination=destination)

    paginator = Paginator(tours, 8)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context = {
        'title': destination.title,
        'tours': qs
    }
    return render(request, 'core/destinations.html', context)


def tours_view(request):
    popular_tours = models.TourWithPrice.objects.all()
    paginator = Paginator(popular_tours, 8)
    page = request.GET.get('page')
    qs = paginator.get_page(page)

    context = {
        'tours': qs
    }
    return render(request, 'core/tours.html', context)


def tour_with_price_detail(request, tour_id):
    tour = models.TourWithPrice.objects.get(pk=tour_id)
    places = ' — '.join([x.place for x in tour.placestourwithprice_set.all()])
    context = {
        'tour': tour,
        'places': places
    }
    return render(request, 'core/tour_detail.html', context)


def tour_detail(request, slug):
    tour = models.Tour.objects.get(slug=slug)
    context = {
        'tour': tour
    }
    return render(request, 'core/detail.html', context)


def hotels_view(request):
    hotels = models.HotelItem.objects.all()
    paginator = Paginator(hotels, 8)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    context = {
        'tours': qs
    }
    return render(request, 'core/hotels.html', context)


def hotel_detail(request, hotel_slug):
    hotel = models.HotelItem.objects.get(slug=hotel_slug)
    hotels = models.HotelItem.objects.all()
    context = {
        'hotel': hotel,

        'hotels': hotels[:8]
    }
    return render(request, 'core/hotel_detail.html', context)


def search(request):
    query = request.GET.get('q')
    
    tours = models.TourWithPrice.objects.filter(title__iregex=query)
    tours2 = models.Tour.objects.filter(title__iregex=query)
    context = {
        'tours_with_price': tours,
        'tours': tours2
    }
    return render(request, 'core/search_page.html', context)