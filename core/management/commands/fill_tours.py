from django.core.management import BaseCommand
import json
from core.models import Tour


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('temp-data/khiva.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                try:
                    tour = Tour.objects.get(title=item['title'])
                    tour.full_description = item['full_description']
                    tour.full_description2 = item['full_description2']
                    tour.map_link = item['map_link']
                    tour.save()
                    print(f'{tour} - updated')
                except:
                    continue