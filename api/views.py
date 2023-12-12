from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api.models import User, Project, Issue, Comment
from api.serializers import UserSerializer, ProjectSerializer, IssueSerializer, CommentSerializer


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class ProjectViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewSet(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewSet(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
