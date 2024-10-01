import os
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class UserInActive(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class MainBanner(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name = 'Birinchi Sahifa Banneri'
        verbose_name_plural = 'Birinchi Sahifa Bannerilari'

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


class Casting(models.Model):
    class Meta:
        verbose_name = "Kasting Yozuvi"
        verbose_name_plural = "Kasting Yozuvlari"

    text_active = models.TextField()
    text_de_active = models.TextField()

    def __str__(self):
        return self.text_active


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


class About(models.Model):
    class Meta:
        verbose_name_plural = "Biz Haqimizda"
        verbose_name = "Biz Haqimizda"

    image = models.FileField(upload_to='about/')
    content = RichTextField()

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"

    def __str__(self):
        return str(self.id)

    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Feedback(models.Model):
    phone = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


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


class Social(models.Model):
    class Meta:
        verbose_name = "Ijtimoy Tarmoq"
        verbose_name_plural = "Ijtimoy Tarmoqlar"

    facebook_link = models.CharField(max_length=250, null=True, blank=True)
    telegram_link = models.CharField(max_length=250, null=True, blank=True)
    instagram_link = models.CharField(max_length=250, null=True, blank=True)
    youtube_link = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.youtube_link


class Sponsor(models.Model):
    icon = models.FileField(upload_to='sponsors')
    link = models.URLField(max_length=350)

    class Meta:
        verbose_name = "Homiy"
        verbose_name_plural = "Homiylar"
        ordering = ['id']

    def __str__(self):
        return self.icon.name

    @property
    def icon_url(self):
        return f"{settings.BASE_URL}{self.icon.url}"


class Partner(models.Model):
    class Meta:
        verbose_name = "Partnor"
        verbose_name_plural = "Partnorlar"
        ordering = ['id']

    icon = models.FileField(upload_to='partners')
    link = models.URLField(max_length=350)

    @property
    def icon_url(self):
        return f"{settings.BASE_URL}{self.icon.url}"
