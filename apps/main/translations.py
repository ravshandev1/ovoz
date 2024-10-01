from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from .models import About, Season, Banner, Main, Casting, UserInActive, MainBanner
from modeltranslation.translator import register, TranslationOptions


class CustomAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class StackAdmin(TranslationStackedInline):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(Casting)
class CastingAdmin(TranslationOptions):
    fields = ['text_active', 'text_de_active']


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'button_text')


@register(MainBanner)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'button_text')


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(UserInActive)
class BannerTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ['content']


@register(Season)
class AboutTranslationOptions(TranslationOptions):
    fields = ['name']
