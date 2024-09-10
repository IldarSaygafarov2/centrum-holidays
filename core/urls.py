from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('reviews/', views.reviews_view, name="reviews"),
    path('booking/', views.booking_view, name="booking"),
    path('mission/', views.mission_view, name="mission"),
    path('info/', views.tourists_info_view, name='tourists-info'),
    path('tours/', views.tours_view, name='tours'),
    path('tours_with_price/<int:tour_id>/', views.tour_with_price_detail, name='tour_with_price_detail'),
    path('tours/<slug:slug>/', views.tour_detail, name='detail'),
    path('blog/', views.blog_view, name='blog'),
    path('destinations/<slug:slug>/', views.destinations_view, name='destinations'),
    path('hotels/', views.hotels_view, name='hotels'),
    path('hotels/<slug:hotel_slug>', views.hotel_detail, name='hotel_detail'),




    path('send_mail/', views.send_mail, name='send_mail'),
    path('send_username_and_phone/', views.send_username_and_phone, name='send_username_and_phone'),
    path('book_tour/', views.book_tour, name='book_tour'),
    path('book_tour_with_price/', views.book_tour_with_price, name='book_tour_with_price'),
    path('book_hotel/', views.book_hotel, name='book_hotel'),
    path('search/', views.search, name='search')
]
