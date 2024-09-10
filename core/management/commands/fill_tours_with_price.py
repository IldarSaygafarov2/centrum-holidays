import json
import os

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
# from django.template.defaultfilters import slugify
from django.utils.text import slugify

from core.models import TourWithPrice


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('temp-data/tours-with-price.json', mode='r', encoding='utf-8') as file:
            content = json.load(file)
            for item in content:
                with open(os.path.join(
                        settings.BASE_DIR, 'media', 'tours', slugify(os.path.basename(item["preview"]))),
                        'wb') as file2:
                    try:
                        file2.write(requests.get(item["preview"], timeout=(10, 10)).content)
                    except Exception as e:
                        print(e)
                        file2.write(requests.get(item["preview"], timeout=(10, 10)).content)

                obj = TourWithPrice.objects.create(
                    title=item['title'],
                    days=item['days'],
                    nights=item['nights'],
                    price=item['price'],
                    preview=f'tours/{slugify(os.path.basename(item["preview"]))}',
                    slug=slugify(item['title'])
                )
                obj.save()
