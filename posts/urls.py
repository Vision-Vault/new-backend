from django.urls import path
from .views import CategoryList, PostList, PostDetail,UserPostView,DonationCreateView, RatePost, PostUsersRatings
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('categories/<int:pk>/', CategoryList.as_view(), name='category-list'),
    path("user/<int:pk>/",UserPostView.as_view(), name='post-user'),
    path("<int:post_id>/donate/",DonationCreateView.as_view(), name='create-donated'),
    path("<int:post_id>/rate/",RatePost.as_view(), name='post-rate'),
    path("<int:pk>/users-ratings/",PostUsersRatings.as_view(), name='post-users-ratings'),

]
