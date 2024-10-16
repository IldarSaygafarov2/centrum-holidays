from django.contrib import admin
from django.db import models
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget

from .models import HomePageStatic, OurMissionStatic, HotelPageStatic, TourDetailStatic, InfoPageStatic


class BaseStaticContentAdmin(ModelAdmin, TranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


class HomePageStaticAdmin(BaseStaticContentAdmin):
    pass


class OurHomePageStaticAdmin(BaseStaticContentAdmin):
    pass


class HotelPageStaticAdmin(BaseStaticContentAdmin):
    pass


class TourDetailStaticAdmin(BaseStaticContentAdmin):
    pass


class InfoPageStaticAdmin(BaseStaticContentAdmin):
    pass


admin.site.register(HomePageStatic, HomePageStaticAdmin)
admin.site.register(OurMissionStatic, OurHomePageStaticAdmin)
admin.site.register(HotelPageStatic, HotelPageStaticAdmin)
admin.site.register(TourDetailStatic, TourDetailStaticAdmin)
admin.site.register(InfoPageStatic, InfoPageStaticAdmin)