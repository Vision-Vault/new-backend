from rest_framework import generics
from .models import Comment, ChildComment
from .serializers import CommentSerializer, ChildCommentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from .permissions import IsOwnerOrReadOnly


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        post = Post.objects.get(pk=pk) 
        queryset = Comment.objects.filter(project=post)  
        return queryset

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True) 
        return Response(serializer.data)
    
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ChildCommentList(generics.ListCreateAPIView):
    serializer_class = ChildCommentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']  
        comment = Comment.objects.get(pk=pk)  
        queryset = ChildComment.objects.filter(parent_comment=comment) 
        return queryset

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset()  
        serializer = self.get_serializer(queryset, many=True)  
        return Response(serializer.data)

class ChildCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildComment.objects.all()
    serializer_class = ChildCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
