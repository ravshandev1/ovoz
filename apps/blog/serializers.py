from rest_framework import serializers
from .models import Blog, YouTubeVideo


class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['song_name', 'link', 'singer_name', 'season']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'created']

    image = serializers.CharField(source='image_url')


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content', 'created']

    image = serializers.CharField(source='image_url')
