import json
import os

import requests
from django.conf import settings
from django.core.management import BaseCommand
from django.template.defaultfilters import slugify

from core.models import HotelItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 22):
            if i == 1:
                file = open('temp-data/hotels.json', mode='r', encoding='utf-8')
            else:
                file = open(f'temp-data/hotels-{i}.json', mode='r', encoding='utf-8')

            print(f'hotels-{i}.json')
            content = json.load(file)
            for line in content:
                price = int(''.join(list(filter(lambda x: x.isdigit(), line['price']))))
                with open(os.path.join(
                        settings.BASE_DIR, 'media', 'hotels', os.path.basename(line["img"])), 'wb') as file:
                    try:
                        file.write(requests.get(line["img"], timeout=(10, 10)).content)
                    except:
                        file.write(requests.get(line["img"], timeout=(10, 10)).content)

                obj = HotelItem.objects.create(
                    name=line['title'],
                    price=price,
                    preview=f'hotels/{os.path.basename(line["img"])}',
                    slug=slugify(line['title'])
                )
                obj.save()

                print(obj, 'created')

        # hotels = get_hotels('https://canaan.travel/ru/uzbekistan/hotels')
        # for item in hotels:
        #     price = int(''.join(list(filter(lambda x: x.isdigit(), item['price']))))
        #     with open(os.path.join(settings.BASE_DIR, 'me', os.path.basename(item["img"])), 'wb') as file:
        #         file.write(requests.get(item["img"]).content)
        #     obj = Hotel.objects.create(
        #         name=item['title'],
        #         price=price,
        #         preview=f'hotels/{os.path.basename(item["img"])}',
        #         slug=slugify(item['title'])
        #     )
        #     obj.save()
        #     print(obj, 'created')

