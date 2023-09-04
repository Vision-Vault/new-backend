from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer,detailUserSerializer
from rest_framework.permissions import AllowAny

class CustomUserList(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    print("queryset:",queryset)
    serializer_class = CustomUserSerializer
    permission_class = [AllowAny]

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = detailUserSerializer
