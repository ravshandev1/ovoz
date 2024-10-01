from django.contrib import admin
from .models import User, Application, Teacher, Participant, Winner, VerifyPhone
from .translations import CustomAdmin


# from main.models import Season


@admin.register(Winner)
class WinnerAdmin(CustomAdmin):
    list_display = ['title']

    def save_model(self, request, obj, *args, **kwargs):
        existed_obj = Winner.objects.last()
        if existed_obj and obj.id != existed_obj.id:
            self.message_user(request, level='ERROR',
                              message="Yangi g'olibni qo'sholmaysiz! Eskisini o'zgartiring!")
        else:
            obj.save()


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'for_kids', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'for_kids']


@admin.register(Teacher)
class TeacherAdmin(CustomAdmin):
    list_display = ['name', 'season']


@admin.register(Participant)
class ParticipantAdmin(CustomAdmin):
    list_display = ['name', 'season', 'teacher', 'is_active']
    list_filter = ['teacher', 'season']

    # @staticmethod
    # def ovozlar_soni(obj):
    #     return obj.voices.count()


# @admin.register(Voice)
# class VoiceAdmin(admin.ModelAdmin):
#
#     def changelist_view(self, request, extra_context=None):
#         response = super().changelist_view(request, extra_context)
#         ls = list()
#         for i in Season.objects.all():
#             s = dict()
#             s['id'] = i.id
#             s['name'] = i.name
#             vt = list()
#             pars = Participant.objects.filter(season=i)
#             for j in i.voice_times.all():
#                 vc = dict()
#                 vc['id'] = j.id
#                 vc['time'] = j.time.strftime('%d/%m/%Y %H:%M')
#                 vc['is_active'] = j.is_active
#                 v = list()
#                 for k in pars:
#                     vr = dict()
#                     vr['name'] = k.name
#                     vr['count'] = j.voices.filter(participant=k).count()
#                     v.append(vr)
#                 v.sort(key=lambda x: x['count'], reverse=True)
#                 vc['voices'] = v
#                 vc['count'] = j.voices.count()
#                 vt.append(vc)
#             s['voice_times'] = vt
#             ls.append(s)
#         response.context_data['seasons'] = ls
#         response.context_data['users'] = User.objects.exclude(phone='admin').count()
#         response.context_data['apps'] = Application.objects.count()
#         return response
#
#     change_list_template = 'dashboard.html'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
@admin.register(VerifyPhone)
class VerifyPhoneAdmin(admin.ModelAdmin):
    list_display = ['phone', 'code']