from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns

schema_view = get_schema_view(
    openapi.Info(
        title='Swagger Doc for The Voice',
        description="This is The Voice project API",
        default_version='v1',
        terms_of_service='https://www.ravshandev.uz',
        contact=openapi.Contact(email="ravshangiyosov2002@gmail.com"),
        license=openapi.License(name='The Voice License'),
    ),
    url=settings.BASE_URL,
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

urlpatterns += [
    *i18n_patterns(path('api/v1/', include('apps.urls')))
]
