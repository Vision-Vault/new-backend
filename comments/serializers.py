from rest_framework import serializers
from .models import Comment, ChildComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 0

    def __init__(self, instance=None, data=None, **kwargs):
        if data :
            setattr(self.Meta , 'depth', 0)
        else:
            setattr(self.Meta , 'depth', 2)

        super(CommentSerializer, self).__init__(instance ,data, **kwargs)

class ChildCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildComment
        fields = '__all__'
        depth = 0

    def __init__(self, instance=None, data=None, **kwargs):
        if data :
            setattr(self.Meta , 'depth', 0)
        else:
            setattr(self.Meta , 'depth', 2)

        super(ChildCommentSerializer, self).__init__(instance ,data, **kwargs)
