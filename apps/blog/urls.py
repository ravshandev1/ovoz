from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogAPI.as_view()),
    path('<int:pk>/', views.BlogDetailAPI.as_view()),
    path('youtube-videos/', views.YouTubeVideoAPI.as_view()),
]
