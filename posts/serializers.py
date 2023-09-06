from rest_framework import serializers
from .models import Category, Post , Donation, Rating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 0

    def __init__(self, instance=None, data=None, **kwargs):
        if data :
            setattr(self.Meta , 'depth', 0)
        else:
            setattr(self.Meta , 'depth', 2)

        super(PostSerializer, self).__init__(instance ,data, **kwargs)


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('user', 'amount')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
        depth = 0

    def __init__(self, instance=None, data=None, **kwargs):
        if data :
            setattr(self.Meta , 'depth', 0)
        else:
            setattr(self.Meta , 'depth', 2)

        super(RatingSerializer, self).__init__(instance ,data, **kwargs)
