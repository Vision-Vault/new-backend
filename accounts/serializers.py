from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'profile_picture','bio', 'email')

class detailUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'profile_picture', 'bio', 'email')
