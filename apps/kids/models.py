from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from blog.models import Blog
import os


class Banner(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = "Kasting Bannerlar"
        verbose_name = "Kasting Banner"

    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='banner')
    text = models.TextField()
    is_active = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"


class Casting(models.Model):
    class Meta:
        verbose_name = "Kasting Yozuvi"
        verbose_name_plural = "Kasting Yozuvlari"

    text_active = models.TextField()
    text_de_active = models.TextField()

    def __str__(self):
        return self.text_active


class Season(models.Model):
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Mavsumlar"
        verbose_name = "Mavsum"

    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VoiceTime(models.Model):
    class Meta:
        verbose_name_plural = "Ovoz berish Vaqtlari"
        verbose_name = "Ovoz berish Vaqti"

    season = models.ForeignKey(Season, models.CASCADE, 'voice_times')
    time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.time.strftime("%d/%m/%Y %H:%M")


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


class Main(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name = 'Asosiy Sahifa Banneri'
        verbose_name_plural = 'Asosiy Sahifa Bannerilari'

    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='main')
    text = models.TextField()
    button_text = models.CharField(max_length=250)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"


class Teacher(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = 'Uztoz'
        verbose_name_plural = 'Uztozlar'

    season = models.ForeignKey(Season, models.CASCADE, 'teachers')
    name = models.CharField(max_length=250)
    main_page_image = models.FileField(upload_to='teachers/')
    image = models.FileField(upload_to='teachers')
    bio = RichTextField()
    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    twitter_link = models.CharField(max_length=250, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)
    telegram_link = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"

    @property
    def main_page_image_url(self):
        return f"{settings.BASE_URL}{self.main_page_image.url}"


class Participant(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name = 'Ishtirokchi'
        verbose_name_plural = 'Ishtirokchilar'

    teacher = models.ForeignKey(Teacher, models.CASCADE, 'participants')
    season = models.ForeignKey(Season, models.CASCADE, 'participants')
    name = models.CharField(max_length=250)
    image = models.FileField(upload_to='participants')
    bio = RichTextField()
    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    twitter_link = models.CharField(max_length=250, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)
    telegram_link = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"


class Winner(models.Model):
    class Meta:
        verbose_name = "G'olib"
        verbose_name_plural = "G'oliblar"

    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='winner')
    blog = models.ForeignKey(Blog, models.SET_NULL, 'kids_winners', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"
