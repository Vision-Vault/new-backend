from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'profile_picture', 'bio', 'email')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        print("password:",password)

        user = CustomUser(**validated_data)

        if password:
            user.set_password(password)
            print("userrr", user)

        print("userrr", user)
        print("333333333333333",type(validated_data['profile_picture']))
        print("1111111111111",validated_data['profile_picture'])
        user.save()
        return user


class detailUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'profile_picture', 'bio', 'email')
