from rest_framework import serializers
from .models import Feedback, VoiceTime, Season, Social, About, Banner, Main, MainBanner


class SponsorAndPartnerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    icon = serializers.CharField(source='icon_url')
    link = serializers.CharField()


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = ['title', 'image', 'text', 'button_text', 'link']

    image = serializers.CharField(source='image_url')


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title', 'image', 'text', 'button_text', 'link']

    image = serializers.CharField(source='image_url')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'text', 'image']

    image = serializers.CharField(source='image_url')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['image', 'content']

    image = serializers.CharField(source='image_url')


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'name']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['phone', 'email', 'message']


class VoiceTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceTime
        fields = ['time']
