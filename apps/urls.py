from django.urls import path, include

urlpatterns = [
    path("user/", include('user.urls')),
    path("blog/", include('blog.urls')),
    path("main/", include('main.urls')),
    path("kids/", include('kids.urls')),
]
