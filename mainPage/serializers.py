from rest_framework import serializers
from .models import Profile, Server, CityPositions
from django.contrib.auth.models import User


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = '__all__'


class CityPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityPositions
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')
