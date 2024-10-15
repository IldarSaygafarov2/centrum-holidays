from typing import Any
from django.core.management import BaseCommand

from core.models import Tour


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        tours = Tour.objects.all()
        key = 'Centrum Holidays'
        for tour in tours:
            if tour.full_description2 is None:
                continue

            if key in tour.full_description2:
                tour.full_description2 = tour.full_description2.replace(
                    key, 'Canaan Travel')
                tour.save()

        # if key in tour.:
        # print(tour)
