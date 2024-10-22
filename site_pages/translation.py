from modeltranslation.translator import translator, TranslationOptions

from .models import HomePageStatic, OurMissionStatic, HotelPageStatic, TourDetailStatic, InfoPageStatic


class HomePageStaticTranslationOptions(TranslationOptions):
    fields = [
        'hero_title',
        'hero_subtitle',
        'section_title_1',
        'section_title_2',
        'special_offer_text',
        'special_offer_text_2',
        'we_recommend_title',
        'know_more_block',
        'know_more_block_2_title',
        'know_more_block_2_text',
        'advantages_title',
        'email_resend_title',
        'booking_block_title',
        'booking_block_text',
        'our_partners_title',
        'footer_text',
    ]


class OurMissionStaticTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_content')


class HotelPageStaticTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_content')


class TourDetailStaticTranslationOptions(TranslationOptions):
    fields = ('text', 'price_include_block')


class InfoPageStaticTranslationOptions(TranslationOptions):
    fields = ('page_title', 'page_content',)


translator.register(HomePageStatic, HomePageStaticTranslationOptions)
translator.register(OurMissionStatic, OurMissionStaticTranslationOptions)
translator.register(HotelPageStatic, HotelPageStaticTranslationOptions)
translator.register(TourDetailStatic, TourDetailStaticTranslationOptions)
translator.register(InfoPageStatic, InfoPageStaticTranslationOptions)