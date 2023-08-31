from django.urls import path
from .views import CategoryList, PostList, PostDetail,UserPostView

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('categories/<int:pk>/', CategoryList.as_view(), name='category-list'),
    path("user/<int:pk>/",UserPostView.as_view(), name='post-user')
]