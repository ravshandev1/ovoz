from django.contrib import admin
from datetime import datetime
from .models import Feedback, VoiceTime, Season, Social, About, Banner, Main, Casting, Sponsor, Partner, MainBanner, UserInActive
from .translations import CustomAdmin


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'icon']


@admin.register(Casting)
class CastingAdmin(CustomAdmin):
    list_display = ['id']

    def save_model(self, request, obj, *args, **kwargs):
        existed_obj = Casting.objects.last()
        if existed_obj and obj.id != existed_obj.id:
            self.message_user(request, level='ERROR',
                              message="Yangi kasting textini qo'sholmaysiz! Eskisini o'zgartiring!")
        else:
            obj.save()


@admin.register(Main)
class MainAdmin(CustomAdmin):
    list_display = ['title', 'button_text', 'link']


@admin.register(MainBanner)
class MainAdmin(CustomAdmin):
    list_display = ['title', 'button_text', 'link']


@admin.register(Banner)
class BannerAdmin(CustomAdmin):
    list_display = ['title', 'is_active']


@admin.register(About)
class AboutAdmin(CustomAdmin):
    list_display = ['id', 'image']

    def save_model(self, request, obj, *args, **kwargs):
        existed_obj = About.objects.last()
        if existed_obj and obj.id != existed_obj.id:
            self.message_user(request, level='ERROR',
                              message="Yangi about qo'sholmaysiz! Eskisini o'zgartiring!")
        else:
            obj.save()


@admin.register(Season)
class SeasonAdmin(CustomAdmin):
    list_display = ['name', 'is_active', 'ishritokchilar_soni']

    @staticmethod
    def ishritokchilar_soni(obj):
        return obj.participants.count()

    def save_model(self, request, obj, *args, **kwargs):
        if obj.is_active and Season.objects.exclude(id=obj.id).exclude(is_active=False).exists():
            self.message_user(request, level="Error",
                              message="Aktiv Mavsum mavjud! Avval eski aktiv mavsumnu deactivate qilib qo'ying!")
        else:
            obj.save()

    def delete_model(self, request, obj, *args, **kwargs):
        if obj.is_active:
            self.message_user(request, level="Error",
                              message="Siz aktiv mavsumni o'chirmoqchisiz! Avval deactivate qilib qo'ying!")
        else:
            obj.delete()


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['phone', 'is_read', 'created_at']
    list_filter = ['created_at', 'is_read']


@admin.register(VoiceTime)
class VoiceTimeAdmin(admin.ModelAdmin):
    list_display = ['season', 'time', 'is_active']

    def save_model(self, request, obj, *args, **kwargs):
        if (obj.is_active and obj.time > datetime.now().astimezone()) and VoiceTime.objects.exclude(
                id=obj.id).exclude(is_active=False).exclude(time__lt=datetime.now().astimezone()).exists():
            self.message_user(request, level="Error",
                              message="Aktiv Time mavjud! Avval eski aktiv timeni deactive qilib qo'ying!")
        else:
            obj.save()

    def delete_model(self, request, obj, *args, **kwargs):
        if obj.is_active and (obj.time.astimezone() > datetime.now().astimezone()):
            self.message_user(request, level="Error",
                              message="Vaqti tugamagan aktiv timeni o'chirib bo'lmaydi! Avval timeni tugating!")
        else:
            obj.delete()


admin.site.register([Social, UserInActive])
