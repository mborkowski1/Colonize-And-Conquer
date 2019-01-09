from rest_framework import viewsets
from .models import Alliance, Forum, SubForum, Topic, PostForum
from .serializers import AllianceSerializer, ForumSerializer, SubForumSerializer, TopicSerializer, PostForumSerializer


class AllianceViewSet(viewsets.ModelViewSet):
    queryset = Alliance.objects.all()
    serializer_class = AllianceSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer


class SubForumViewSet(viewsets.ModelViewSet):
    queryset = SubForum.objects.all()
    serializer_class = SubForumSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class PostForumViewSet(viewsets.ModelViewSet):
    queryset = PostForum.objects.all()
    serializer_class = PostForumSerializer
