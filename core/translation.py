from modeltranslation.translator import register, TranslationOptions

from . import models


@register(models.Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('author', 'text')


@register(models.HotelItem)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(models.Bun)
class BunTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'full_description', 'full_description2')


@register(models.TourWithPrice)
class TourWithPriceTranslationOptions(TranslationOptions):
    fields = ('title', 'full_description', 'season')


@register(models.PlacesTourWithPrice)
class PlacesTourWithPriceTranslationOptions(TranslationOptions):
    fields = ('place',)


@register(models.DayTourWithPrice)
class DayTourWithPriceTranslationOptions(TranslationOptions):
    fields = ('name', 'descr')


@register(models.AddonTourWithPrice)
class AddonTourWithPriceTranslationOptions(TranslationOptions):
    fields = ('name', 'descr')


@register(models.TourCondition)
class TourConditionTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.TourPriceInclude)
class TourPriceIncludeTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.TourPriceDoesNotInclude)
class TourPriceDoesNotIncludeTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(models.Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(models.Destination)
class DestinationTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description')


@register(models.Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'excerpt')
