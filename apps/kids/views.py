from rest_framework import generics, response
from datetime import datetime
from main.paginations import CustomLimitOffsetPagination
from .serializers import TeacherSerializer, ParticipantSerializer, ParticipantDetailSerializer, \
    TeacherDetailSerializer, WinnerSerializer, YouTubeVideoSerializer, MainSerializer, VoiceTimeSerializer, \
    BannerSerializer, SeasonSerializer
from .models import Teacher, Participant, Winner, VoiceTime, YouTubeVideo, Casting, Season, Main, Banner


class VoiceTimeAPI(generics.GenericAPIView):
    serializer_class = VoiceTimeSerializer

    def get(self, request, *args, **kwargs):
        obj = VoiceTime.objects.filter(is_active=True, time__gt=datetime.now().astimezone(),
                                       season__is_active=True).first()
        if obj is not None:
            serializer = self.get_serializer(obj)
            return response.Response({'success': True, 'data': serializer.data})
        else:
            return response.Response({'success': False}, status=400)


class CastingAPI(generics.GenericAPIView):
    queryset = Casting.objects.all()
    serializer_class = MainSerializer

    def get(self, request, *args, **kwargs):
        obj = self.queryset.first()
        if Banner.objects.filter(is_active=True).exists():
            return response.Response({'text': obj.text_de_active})
        return response.Response({'text': obj.text_active})


class MainAPI(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class BannerAPI(generics.GenericAPIView):
    serializer_class = BannerSerializer

    def get(self, request, *args, **kwargs):
        obj = Banner.objects.filter(is_active=True).first()
        if obj is None:
            return response.Response(
                {'success': False, 'message_ru': 'Регистрация завершена', 'message_uz': "Ro'yxatga olish tugagan",
                 'message_en': 'Registration is completed'}, status=400)
        serializer = self.get_serializer(obj)
        return response.Response(serializer.data)


class SeasonCheckAPI(generics.GenericAPIView):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    def get(self, request, *args, **kwargs):
        if self.queryset.filter(is_active=True).exists():
            return response.Response({'success': True})
        else:
            return response.Response({'success': False}, status=400)


class SeasonAPI(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class YouTubeVideoAPI(generics.ListAPIView):
    serializer_class = YouTubeVideoSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        season = self.request.query_params.get('season')
        if season is not None:
            qs = YouTubeVideo.objects.filter(season_id=season)
        else:
            qs = YouTubeVideo.objects.all()
        return qs


class WinnerAPI(generics.GenericAPIView):
    serializer_class = WinnerSerializer
    queryset = Winner.objects.all()

    def get(self, request, *args, **kwargs):
        obj = self.queryset.first()
        serializer = WinnerSerializer(obj)
        return response.Response(serializer.data)


class TeacherAPI(generics.GenericAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        data = list()
        season = Season.objects.filter(is_active=True).first()
        if season is None:
            return response.Response({'success': False, 'message_ru': 'В настоящее время сезон активов недоступен!',
                                      'message_uz': "Hozirda aktiv season mavjud emas!",
                                      'message_en': "The asset season is currently unavailable!"}, status=400)
        if self.request.user:
            user_id = self.request.user.id
        else:
            user_id = None
        for i in Teacher.objects.filter(season=season).all():
            dt = TeacherSerializer(i).data
            ls = list()
            for j in i.participants.filter(season=season):
                d = ParticipantSerializer(j).data
                # if Voice.objects.filter(user_id=user_id, participant=j).exists():
                #     d['was_voted'] = True
                # else:
                #     d['was_voted'] = False
                ls.append(d)
            dt['participants'] = ls
            data.append(dt)
        return response.Response(data)


class TeacherFilterAPI(generics.ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_queryset(self):
        return Teacher.objects.filter(season_id=self.request.query_params.get('season'))


class ParticipantAPI(generics.ListAPIView):
    serializer_class = ParticipantSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        teacher = self.request.query_params.get('teacher', None)
        if teacher is None:
            return Participant.objects.filter(season_id=self.request.query_params.get('season'))
        else:
            return Participant.objects.filter(season_id=self.request.query_params.get('season'), teacher_id=teacher)


class TeacherDetailAPI(generics.RetrieveAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = TeacherDetailSerializer(obj).data
        data['participants'] = ParticipantSerializer(obj.participants.all(), many=True).data
        return response.Response(data)


class ParticipantDetailAPI(generics.RetrieveAPIView):
    serializer_class = ParticipantDetailSerializer
    queryset = Participant.objects.all()
