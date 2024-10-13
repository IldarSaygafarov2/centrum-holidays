from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline as UnfoldTabularInline

from . import models


# Register your models here.

class ReviewAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('author', 'text')


class PlacesTourWithPriceInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.PlacesTourWithPrice
    extra = 1


class DayTourWithPriceInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.DayTourWithPrice
    extra = 1


class AddonTourWithPriceInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.AddonTourWithPrice
    extra = 1


class TourConditionInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.TourCondition
    extra = 1


class TourHotelInline(UnfoldTabularInline):
    model = models.TourHotel
    extra = 1


class TourPriceIncludeInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.TourPriceInclude
    extra = 1


class TourPriceDoesNotIncludeInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.TourPriceDoesNotInclude
    extra = 1


class PriceByHumanTourInline(UnfoldTabularInline):
    model = models.PriceByHumanTour
    extra = 1
# TourWithPrice inlines end


class TourAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('title', 'preview', 'is_popular', 'is_recommended', 'destination')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('destination',)
    search_fields = ['title']
    list_editable = ('is_popular', 'is_recommended')


class TourWithPriceAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('title', 'price', 'days', 'nights', 'is_popular', 'is_recommended')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        PlacesTourWithPriceInline,
        DayTourWithPriceInline,
        AddonTourWithPriceInline,
        TourConditionInline,
        TourHotelInline,
        TourPriceIncludeInline,
        TourPriceDoesNotIncludeInline,
        PriceByHumanTourInline,

    ]
    list_editable = ('is_popular', 'is_recommended')


class ArticleAdmin(TranslationAdmin, ModelAdmin):
    pass


class DestinationAdmin(TranslationAdmin, ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AdvantageAdmin(TranslationAdmin, ModelAdmin):
    pass


class HotelBunInline(UnfoldTabularInline, TranslationTabularInline):
    model = models.Bun
    extra = 1


class HotelImageGalleryInline(admin.TabularInline):
    model = models.HotelGallery
    extra = 1


class HotelAdmin(TranslationAdmin, ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        HotelBunInline,
        HotelImageGalleryInline
    ]


admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Client)
admin.site.register(models.HotelItem, HotelAdmin)
admin.site.register(models.Advantage, AdvantageAdmin)
admin.site.register(models.Destination, DestinationAdmin)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.TourWithPrice, TourWithPriceAdmin)
admin.site.register(models.Article, ArticleAdmin)
