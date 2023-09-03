from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerAndUpdateFields
from .models import Category, Post,Donation
from .serializers import CategorySerializer, PostSerializer,DonationSerializer
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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerAndUpdateFields]



class DonationCreateView(APIView):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        user = request.user

        if post.allowed_donors > 0 and post.funding_goal > 0:
            donation_amount = float(request.data.get('amount', 0))

            if donation_amount <= post.funding_goal:
                post.allowed_donors -= 1
                post.funding_goal =float(post.funding_goal) - float(donation_amount)
                donation = Donation.objects.create(user=user, post=post, amount=donation_amount)
                post.save()
                serializer = DonationSerializer(donation)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'detail': 'Unable to make a donation.'}, status=status.HTTP_400_BAD_REQUEST)



