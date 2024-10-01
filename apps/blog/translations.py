from modeltranslation.translator import register, TranslationOptions
from .models import Blog
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


@register(Blog)
class BlogTranslation(TranslationOptions):
    fields = ['title', 'content']
