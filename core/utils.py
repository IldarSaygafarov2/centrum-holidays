import time
import requests
from bs4 import BeautifulSoup
from os.path import basename
import json
from django.conf import settings


def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, 'html.parser')


def get_tours(url):
    soup = get_soup(url)
    wrapper = soup.find('div', class_='show-objects-container')
    res = []
    for item in wrapper.find_all('div', class_='show-objects-item'):
        title = item.find('a', class_='show-objects-title').get_text(strip=True)
        link = item.find('a', class_='show-objects-title')['href']
        print(title)
        try:
            tour_soup = get_soup(link)
        except:
            tour_soup = get_soup(link)
        wrapper = tour_soup.find('div', class_='wprt-container')
        txt = []
        for i in wrapper:
            if not i.name:
                continue
            if not i.find('iframe'):
                txt.append(str(i))
            else:
                txt.append('')

        if '' in txt:
            descr_1 = ''.join(txt[:txt.index('')])
            descr_2 = ''.join(txt[txt.index(''):])
        else:
            descr_1 = ''.join(txt[:len(txt)//2])
            descr_2 = ''.join(txt[len(txt)//2:])

        map_link = wrapper.find('iframe')
        if map_link:
            map_link = map_link.get('data-src')
        else:
            map_link = ''
        res.append({
            'title': title,
            'link': link,
            'full_description': descr_1,
            'full_description2': descr_2,
            'map_link': map_link
        })
        time.sleep(5)
    return res


# tashkent_tours = get_tours('https://canaan.travel/ru/uzbekistan/bukhara')

# with open('../temp-data/khiva.json', mode='w', encoding='utf-8') as file:
#     json.dump(tashkent_tours, file, indent=4, ensure_ascii=False)


def get_hotels_last_page(url):
    soup = get_soup(url)
    wrap = soup.find('div', class_='show-hotels-pagination')
    pages = [i.get_text(strip=True) for i in wrap.find_all('a')][-1]
    return int(pages)


# https://canaan.travel/ru/uzbekistan/hotels

def get_hotels(url, page_num=1):
    res = []

    if page_num == 1:
        soup = get_soup(url)
    else:
        soup = get_soup(url + f'/page/{page_num}')

    wrap = soup.find('div', class_='show-hotels-container')
    for hotel in wrap.find_all('div', class_='show-hotels-item'):
        title = hotel.find('a', class_='show-hotels-title').get_text(strip=True)
        href = hotel.find('a', class_='show-hotels-title')['href']
        print(title)
        try:
            inner = get_soup(href)
        except:
            inner = get_soup(href)
        
        buns = [bun.get_text(strip=True) for bun in inner.find('ul', class_='wb-list-amenities').find_all('li')]
        description = inner.find('div', class_='wprt-container')
        inner_images = inner.find('div', class_='service-gallery-single').find_all('img')
        inner_images = [i['src'] for i in inner_images]
        
        price = hotel.find('div', class_='show-hotels-cost').get_text(strip=True).split('/')[0]
        img = hotel.find('img')['data-src']
    
        res.append({
            'title': title,
            'price': price,
            'buns': buns,
            'description': str(description),
            'inner_images': inner_images,
            'img': img
        })
    return res


hotels = get_hotels('https://canaan.travel/ru/uzbekistan/hotels/page/3')
with open('../temp-data/hotels-3.json', mode='w', encoding='utf-8') as file:
    json.dump(hotels, file, indent=4, ensure_ascii=False)


# https://saftravel.uz/ru/uzbekistan/tours
def get_tours_with_price(url):
    soup = get_soup(url)
    res = []
    items = soup.find('div', class_='tourview-tour-container').find_all('a', class_='tourview-tour-item')
    for item in items:
        title = item.find('div', class_='tourview-tour-title').get_text(strip=True)
        days_nights = item.find('div', class_='tourview-tour-duration').get_text(strip=True)
        days, nights = 0, 0
        if days_nights:
            days, nights = [int(x.split()[0]) for x in days_nights.split('/')]

        price = item.find('div', class_='tourview-tour-cost').find('div', class_='tourview-tour-cost').get_text(strip=True)

        preview = item.find('img')['data-src']
        res.append({
            'title': title,
            'days': days,
            'nights': nights,
            'price': price,
            'preview': preview
        })
    return res


# tours = get_tours_with_price('https://saftravel.uz/ru/uzbekistan/tours')
# with open('../temp-data/tours-with-price.json', mode='w', encoding='utf-8') as file:
#     json.dump(tours, file, indent=4, ensure_ascii=False)