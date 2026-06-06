from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author']
    serializer_class = PostSerializer

    lookup_field = 'slug'