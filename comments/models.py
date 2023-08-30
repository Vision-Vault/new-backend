from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post
from django.urls import reverse_lazy, reverse
from accounts.models import CustomUser

# Create your models here.

class Shared(models.Model):
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True

class Comment(Shared):
    project=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='all_comments')
    user=models.ForeignKey(CustomUser,related_name='comments',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class ChildComment(Shared):
    parent_comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='child_comments')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

