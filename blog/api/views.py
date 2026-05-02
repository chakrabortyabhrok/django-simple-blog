from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import status

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class PostDetailView(APIView):
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, slug):
        post = self.get_object(slug)

        if post is None:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, slug):
        post = self.get_object(slug)

        if post is None:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, slug):
        post = self.get_object(slug)

        serializer = PostSerializer(post, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, slug):
        post = self.get_object(slug)

        if post is None:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response({'message': "Post deleted successfuly"}, status=status.HTTP_204_NO_CONTENT)
    
    