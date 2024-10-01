from modeltranslation.translator import register, TranslationOptions
from .models import Teacher, Participant, Notification, Winner
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


@register(Winner)
class WinnerTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Notification)
class NotificationAdmin(TranslationOptions):
    fields = ['text']


@register(Teacher)
class JuryTranslationOptions(TranslationOptions):
    fields = ('name', 'bio')


@register(Participant)
class ParticipantTranslationOptions(TranslationOptions):
    fields = ('name', 'bio')
