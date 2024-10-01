from django.urls import path
from . import views
urlpatterns = [
    path('me/', views.UserAPI.as_view()),
    path('delete/', views.UserDeleteAPI.as_view()),
    path('winner/', views.WinnerAPI.as_view()),
    path('notifications/', views.NotificationAPI.as_view()),
    path('register/', views.RegisterAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('verify-phone/', views.VerifyPhoneAPI.as_view()),
    path('teachers/', views.TeacherAPI.as_view()),
    path('teacher-filter/', views.TeacherFilterAPI.as_view()),
    path('participants/', views.ParticipantAPI.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetailAPI.as_view()),
    path('participant/<int:pk>/', views.ParticipantDetailAPI.as_view()),
    path('application/', views.ApplicationAPI.as_view()),
]
