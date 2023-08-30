from django.urls import path
from .views import CommentList, CommentDetail, ChildCommentList, ChildCommentDetail

urlpatterns = [
    path('<int:pk>/', CommentList.as_view(), name='comment-list'),
    path('detail/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('child-comments/<int:pk>/', ChildCommentList.as_view(), name='child-comment-list'),
    path('child-detail/<int:pk>/', ChildCommentDetail.as_view(), name='child-comment-detail'),
]
