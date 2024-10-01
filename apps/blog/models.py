import os
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from main.models import Season


class Blog(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='blog/')
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"


class YouTubeVideo(models.Model):
    class Meta:
        verbose_name = "YouTube Video"
        verbose_name_plural = "YouTube Videolari"
        ordering = ['-id']

    season = models.ForeignKey(Season, models.CASCADE, 'youtube_videos')
    song_name = models.CharField(max_length=250)
    singer_name = models.CharField(max_length=250)
    link = models.URLField()

    def __str__(self):
        return self.link
