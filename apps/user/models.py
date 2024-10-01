import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from main.models import Season, VoiceTime
from blog.models import Blog
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        user = self.model(**kwargs)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, password=None, **kwargs):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(**kwargs)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(null=True)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class Notification(models.Model):
    user = models.ForeignKey(User, models.CASCADE, 'notifications')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Application(models.Model):
    class Meta:
        verbose_name = 'Kasting'
        verbose_name_plural = 'Kastinglar'

    STATUS_CHOICES = (
        (1, 'Yuborildi'),
        (2, 'Tekshirilmoqda'),
        (3, 'Qabul qilindi'),
        (4, 'Rad qilindi'),
    )
    user = models.ForeignKey(User, models.CASCADE)
    season = models.ForeignKey(Season, models.CASCADE)
    for_kids = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    video = models.FileField(upload_to='application_videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        os.remove(self.video.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        text_uz = "AriAriza holati: "
        text_ru = "Статус заявки: "
        text_en = "Application status: "
        if self.status == 2:
            text_uz += "Tekshirilmoqda"
            text_ru += "Проверка"
            text_en += "Checking"
        elif self.status == 3:
            text_uz += "Qabul qilindi"
            text_ru += "Принято"
            text_en += "Accepted"
        elif self.status == 4:
            text_uz += "Rad qilindi"
            text_ru += "Отказано"
            text_en += "Rejected"
        Notification.objects.create(user=self.user, text_ru=text_ru, text_uz=text_uz, text_en=text_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class VerifyPhone(models.Model):
    phone = models.CharField(max_length=250)
    code = models.CharField(max_length=250)

    def __str__(self):
        return self.phone


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


# class Voice(models.Model):
#     class Meta:
#         verbose_name = 'Ovoz'
#         verbose_name_plural = 'Ovozlar'
#
#     time = models.ForeignKey(VoiceTime, models.CASCADE, 'voices')
#     user = models.ForeignKey(User, models.CASCADE, 'voices')
#     participant = models.ForeignKey(Participant, models.CASCADE, 'voices')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.participant.name


class Winner(models.Model):
    class Meta:
        verbose_name = "G'olib"
        verbose_name_plural = "G'oliblar"

    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='winner')
    blog = models.ForeignKey(Blog, models.SET_NULL, 'winners', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return f"{settings.BASE_URL}{self.image.url}"
