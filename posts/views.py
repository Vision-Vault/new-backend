from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework.response import Response
from accounts.models import CustomUser



class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        category = Category.objects.get(pk=pk) 
        queryset = Post.objects.filter(category=category).filter(status=Post.ACTIVE)
        return queryset

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True) 
        return Response(serializer.data)
    
class UserPostView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        user = CustomUser.objects.get(pk=pk) 
        queryset = Post.objects.filter(creator=user)
        return queryset

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True) 
        return Response(serializer.data)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=Post.ACTIVE)
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

