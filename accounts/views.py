from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer,detailUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

class CustomUserList(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    print("queryset:",queryset)
    serializer_class = CustomUserSerializer
    permission_class = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = detailUserSerializer
    parser_classes = [MultiPartParser, FormParser]

