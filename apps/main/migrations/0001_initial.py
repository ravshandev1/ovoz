# Generated by Django 5.0.3 on 2024-10-01 20:42

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='about/')),
                ('content', ckeditor.fields.RichTextField()),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('content_uz', ckeditor.fields.RichTextField(null=True)),
                ('content_en', ckeditor.fields.RichTextField(null=True)),
            ],
            options={
                'verbose_name': 'Biz Haqimizda',
                'verbose_name_plural': 'Biz Haqimizda',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_uz', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('image', models.FileField(upload_to='banner')),
                ('text', models.TextField()),
                ('text_ru', models.TextField(null=True)),
                ('text_uz', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Kasting Banner',
                'verbose_name_plural': 'Kasting Bannerlar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_active', models.TextField()),
                ('text_active_ru', models.TextField(null=True)),
                ('text_active_uz', models.TextField(null=True)),
                ('text_active_en', models.TextField(null=True)),
                ('text_de_active', models.TextField()),
                ('text_de_active_ru', models.TextField(null=True)),
                ('text_de_active_uz', models.TextField(null=True)),
                ('text_de_active_en', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Kasting Yozuvi',
                'verbose_name_plural': 'Kasting Yozuvlari',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_uz', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('image', models.FileField(upload_to='main')),
                ('text', models.TextField()),
                ('text_ru', models.TextField(null=True)),
                ('text_uz', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('button_text', models.CharField(max_length=250)),
                ('button_text_ru', models.CharField(max_length=250, null=True)),
                ('button_text_uz', models.CharField(max_length=250, null=True)),
                ('button_text_en', models.CharField(max_length=250, null=True)),
                ('link', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Asosiy Sahifa Banneri',
                'verbose_name_plural': 'Asosiy Sahifa Bannerilari',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_uz', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('image', models.FileField(upload_to='main')),
                ('text', models.TextField()),
                ('text_ru', models.TextField(null=True)),
                ('text_uz', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('button_text', models.CharField(max_length=250)),
                ('button_text_ru', models.CharField(max_length=250, null=True)),
                ('button_text_uz', models.CharField(max_length=250, null=True)),
                ('button_text_en', models.CharField(max_length=250, null=True)),
                ('link', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Birinchi Sahifa Banneri',
                'verbose_name_plural': 'Birinchi Sahifa Bannerilari',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='partners')),
                ('link', models.URLField(max_length=350)),
            ],
            options={
                'verbose_name': 'Partnor',
                'verbose_name_plural': 'Partnorlar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('name_uz', models.CharField(max_length=250, null=True)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Mavsum',
                'verbose_name_plural': 'Mavsumlar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(blank=True, max_length=250, null=True)),
                ('telegram_link', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Ijtimoy Tarmoq',
                'verbose_name_plural': 'Ijtimoy Tarmoqlar',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='sponsors')),
                ('link', models.URLField(max_length=350)),
            ],
            options={
                'verbose_name': 'Homiy',
                'verbose_name_plural': 'Homiylar',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserInActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('text_ru', models.CharField(max_length=500, null=True)),
                ('text_uz', models.CharField(max_length=500, null=True)),
                ('text_en', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoiceTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voice_times', to='main.season')),
            ],
            options={
                'verbose_name': 'Ovoz berish Vaqti',
                'verbose_name_plural': 'Ovoz berish Vaqtlari',
            },
        ),
    ]
