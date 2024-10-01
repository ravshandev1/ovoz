from rest_framework import generics, response
from datetime import datetime
from .serializers import FeedbackSerializer, VoiceTimeSerializer, SeasonSerializer, SocialSerializer, AboutSerializer, \
    BannerSerializer, MainSerializer, SponsorAndPartnerSerializer, MainBannerSerializer
from .models import Feedback, VoiceTime, Season, Social, About, Banner, Main, Casting, Sponsor, Partner, MainBanner


class MainBannerView(generics.ListAPIView):
    serializer_class = MainBannerSerializer
    queryset = MainBanner.objects.all()


class SponsorAPI(generics.ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorAndPartnerSerializer


class PartnerAPI(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = SponsorAndPartnerSerializer


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


class AboutAPI(generics.GenericAPIView):
    serializer_class = AboutSerializer

    def get(self, request, *args, **kwargs):
        about = About.objects.last()
        serializer = self.serializer_class(about)
        return response.Response(serializer.data)


class SocialAPI(generics.GenericAPIView):
    serializer_class = SocialSerializer

    def get(self, request, *args, **kwargs):
        qs = Social.objects.first()
        serializer = self.serializer_class(qs)
        return response.Response(serializer.data)


class SeasonAPI(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class SeasonCheckAPI(generics.GenericAPIView):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    def get(self, request, *args, **kwargs):
        if self.queryset.filter(is_active=True).exists():
            return response.Response({'success': True})
        else:
            return response.Response({'success': False}, status=400)


class FeedbackAPI(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


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
