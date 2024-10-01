from modeltranslation.translator import register, TranslationOptions
from .models import Teacher, Participant, Winner, Season, Banner, Casting, Main
from modeltranslation.admin import TranslationAdmin


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


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'button_text')


@register(Casting)
class CastingAdmin(TranslationOptions):
    fields = ['text_active', 'text_de_active']


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Season)
class AboutTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Winner)
class WinnerTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Teacher)
class JuryTranslationOptions(TranslationOptions):
    fields = ('name', 'bio')


@register(Participant)
class ParticipantTranslationOptions(TranslationOptions):
    fields = ('name', 'bio')
