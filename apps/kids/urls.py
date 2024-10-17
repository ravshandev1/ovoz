from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPI.as_view()),
    path('seasons/', views.SeasonAPI.as_view()),
    path('season-check/', views.SeasonCheckAPI.as_view()),
    path('voice-time/', views.VoiceTimeAPI.as_view()),
    path('banner/', views.BannerAPI.as_view()),
    path('casting-text/', views.CastingAPI.as_view()),
    path('winner/', views.WinnerAPI.as_view()),
    path('teachers/', views.TeacherAPI.as_view()),
    path('teacher-filter/', views.TeacherFilterAPI.as_view()),
    path('participants/', views.ParticipantAPI.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetailAPI.as_view()),
    path('participant/<int:pk>/', views.ParticipantDetailAPI.as_view()),
    path('sponsors/', views.SponsorAPI.as_view()),
    path('partners/', views.PartnerAPI.as_view()),
]
