from rest_framework import generics
from main.paginations import CustomLimitOffsetPagination
from .models import Blog, YouTubeVideo
from .serializers import BlogSerializer, BlogDetailSerializer, YouTubeVideoSerializer


class YouTubeVideoAPI(generics.ListAPIView):
    serializer_class = YouTubeVideoSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        season = self.request.query_params.get('season')
        if season is not None:
            qs = YouTubeVideo.objects.filter(season_id=season)
        else:
            qs = YouTubeVideo.objects.all()
        return qs


class BlogAPI(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CustomLimitOffsetPagination


class BlogDetailAPI(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
