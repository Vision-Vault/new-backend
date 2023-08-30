from rest_framework import serializers
from .models import Comment, ChildComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ChildCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildComment
        fields = '__all__'
