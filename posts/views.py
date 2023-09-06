from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerAndUpdateFields
from .models import Category, Post,Donation, Rating
from .serializers import CategorySerializer, PostSerializer,DonationSerializer,RatingSerializer
from rest_framework.response import Response
from accounts.models import CustomUser
from django.db.models import Sum
from django.db.models import Count
from rest_framework.parsers import MultiPartParser, FormParser





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
    parser_classes = [MultiPartParser, FormParser]

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
    parser_classes = [MultiPartParser, FormParser]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerAndUpdateFields]
    parser_classes = [MultiPartParser, FormParser]

class PostUsersRatings(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerAndUpdateFields]
    serializer_class = RatingSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        post = Post.objects.get(id=pk)
        queryset = Rating.objects.filter(post=post)
        return queryset

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data})

class RatePost(APIView):
    def post(self, request , post_id):
        try:
            args = request.data.copy()
            rating = args.get("rate" , None)
            user_id = args.get("user" , None)

            # Get post record
            post = Post.objects.get(pk=post_id)

            # Get user record
            try:
                user = CustomUser.objects.get(pk=user_id)
            except Exception as error :
                return Response({'error': "You have to login to add you rating on this post"}, status=status.HTTP_400_BAD_REQUEST)


            # Check if rating already provided
            try:
                old_rating = Rating.objects.get(user=user, post=post)
            except Exception as error :
                old_rating = None

            if old_rating == None :
                # Create
                new_rating = Rating.objects.create(user=user, post=post, value=rating)
            else:
                # Update
                new_rating = Rating.objects.filter(user=user, post=post).update(value=rating)

            # Update post rating
            sum_record = Rating.objects.aggregate(Sum('value'))
            count_record = Rating.objects.filter(post = post).values("post_id").annotate(Count("post_id"))
            sum_value = sum_record.get("value__sum",0)
            count_value = count_record[0].get("post_id__count",0)

            #Calculate total rating on post
            total_rating = sum_value/count_value

            # Update post rating
            Post.objects.filter(id=post_id).update(rating=total_rating)

            return Response({'data': "Rating placed successfully!"}, status=status.HTTP_200_OK)

        except Exception as error :
            return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)



    # get rating
    # insert rsting to post

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



