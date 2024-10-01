from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPI.as_view()),
    path('main-banner/', views.MainBannerView.as_view()),
    path('feedback/', views.FeedbackAPI.as_view()),
    path('seasons/', views.SeasonAPI.as_view()),
    path('season-check/', views.SeasonCheckAPI.as_view()),
    path('voice-time/', views.VoiceTimeAPI.as_view()),
    path('socials/', views.SocialAPI.as_view()),
    path('about/', views.AboutAPI.as_view()),
    path('banner/', views.BannerAPI.as_view()),
    path('casting-text/', views.CastingAPI.as_view()),
    path('sponsors/', views.SponsorAPI.as_view()),
    path('partners/', views.PartnerAPI.as_view()),
]
