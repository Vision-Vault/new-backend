from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer,detailUserSerializer

class CustomUserList(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = detailUserSerializer
