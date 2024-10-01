from rest_framework import serializers
from .models import User, Teacher, Participant, Application, Notification, Winner
from main.models import UserInActive


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['title', 'image', 'blog']

    image = serializers.CharField(source='image_url')
    blog = serializers.CharField(source='blog.id')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'text', 'created_at']


#
# class VoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Voice
#         fields = ['participant', 'time', 'user']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['user', 'season', 'for_kids', 'first_name', 'last_name', 'phone', 'city', 'video', 'video_path',
                  'created_at']

    created_at = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    video_path = serializers.CharField(source='video.path', read_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']

    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['guid', 'first_name', 'last_name', 'phone']

    guid = serializers.IntegerField(source='id')


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['guid', 'name', 'image', 'is_active', 'text']

    guid = serializers.IntegerField(source='id')
    text = serializers.SerializerMethodField()
    image = serializers.CharField(source='image_url')

    def get_text(self, obj):
        if obj.is_active:
            return None
        text = UserInActive.objects.first()
        return text.text if text else None


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['guid', 'name', 'image', 'main_image']

    guid = serializers.IntegerField(source='id')
    image = serializers.CharField(source='image_url')
    main_image = serializers.CharField(source='main_page_image_url')


class ParticipantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['guid', 'name', 'image', 'bio', 'is_active', 'twitter_link', 'youtube_link', 'instagram_link',
                  'facebook_link',
                  'telegram_link']

    image = serializers.CharField(source='image_url')
    guid = serializers.IntegerField(source='id')


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['guid', 'name', 'image', 'bio', 'facebook_link', 'instagram_link', 'twitter_link', 'youtube_link',
                  'telegram_link']

    image = serializers.CharField(source='image_url')
    guid = serializers.IntegerField(source='id')
