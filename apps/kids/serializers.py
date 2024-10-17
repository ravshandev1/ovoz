from rest_framework import serializers
from .models import Teacher, Participant, Winner, Main, Banner, Season, VoiceTime, YouTubeVideo
from main.models import UserInActive


class SponsorAndPartnerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    icon = serializers.CharField(source='icon_url')
    link = serializers.CharField()


class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['song_name', 'link', 'singer_name', 'season']
        ref_name = "Kids"


class VoiceTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceTime
        fields = ['time']
        ref_name = 'Kids'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'name']
        ref_name = 'Kids'


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title', 'image', 'text', 'button_text', 'link']
        ref_name = "Kids"

    image = serializers.CharField(source='image_url')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['title', 'text', 'image']
        ref_name = "Kids"

    image = serializers.CharField(source='image_url')


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['guid', 'name', 'image', 'bio', 'facebook_link', 'instagram_link', 'twitter_link', 'youtube_link',
                  'telegram_link']
        ref_name = "Kids"

    image = serializers.CharField(source='image_url')
    guid = serializers.IntegerField(source='id')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['guid', 'name', 'image', 'main_image']
        ref_name = "Kids"

    guid = serializers.IntegerField(source='id')
    image = serializers.CharField(source='image_url')
    main_image = serializers.CharField(source='main_page_image_url')


class ParticipantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['guid', 'name', 'image', 'bio', 'is_active', 'twitter_link', 'youtube_link', 'instagram_link',
                  'facebook_link', 'telegram_link']
        ref_name = "Kids"

    image = serializers.CharField(source='image_url')
    guid = serializers.IntegerField(source='id')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['guid', 'name', 'image', 'is_active', 'text']
        ref_name = "Kids"

    guid = serializers.IntegerField(source='id')
    text = serializers.SerializerMethodField()
    image = serializers.CharField(source='image_url')

    def get_text(self, obj):
        if obj.is_active:
            return None
        text = UserInActive.objects.first()
        return text.text if text else None


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['title', 'image', 'blog']
        ref_name = "Kids"

    image = serializers.CharField(source='image_url')
    blog = serializers.CharField(source='blog.id')
