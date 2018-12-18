from rest_framework import viewsets
from .models import Profile, Server, CityPositions
from .serializers import ProfileSerializer, UserSerializer, ServerSerializer, CityPositionsSerializer
from django.contrib.auth.models import User


class CityPositionsViewSet(viewsets.ModelViewSet):
    queryset = CityPositions.objects.all()
    serializer_class = CityPositionsSerializer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
