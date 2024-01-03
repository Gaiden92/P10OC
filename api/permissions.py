from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from .models import Project, Contributor


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Autoriser les requêtes GET, HEAD ou OPTIONS
        if request.method in permissions.SAFE_METHODS and \
                              request.user.is_authenticated:
            return True

        project_pk = request.data.get('project', None)
        if project_pk:
            project = Project.objects.get(pk=project_pk)
            return project.author == request.user

        return False

    def has_object_permission(self, request, view, obj):
        return obj.project.author == request.user


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        contributors = Contributor.objects.filter(project=obj)
        return contributors.filter(user=request.user)


class IsContributorForIssue(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            try:
                project = Project.objects.get(id=view.kwargs['project_pk'])
            except ObjectDoesNotExist:
                return False
            return project.contributors.filter(user=request.user)

    def has_object_permission(self, request, view, obj):
        contributors = Contributor.objects.filter(project=obj.project)
        return contributors.filter(user=request.user)


class IsAuthorOfIssue(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsContributorForComment(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            try:
                project = Project.objects.get(id=view.kwargs['project_pk'])
            except ObjectDoesNotExist:
                return False
            return project.contributors.filter(user=request.user)

    def has_object_permission(self, request, view, obj):
        contributors = Contributor.objects.filter(project=obj.issue.project)
        return contributors.filter(user=request.user)


class IsAuthorOfComment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
