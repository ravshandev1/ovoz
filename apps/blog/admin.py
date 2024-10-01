from django.contrib import admin
from .models import Blog, YouTubeVideo
from .translations import CustomAdmin


@admin.register(Blog)
class BlogAdmin(CustomAdmin):
    list_display = ['title', 'created']


@admin.register(YouTubeVideo)
class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ['season', 'song_name', 'singer_name']
