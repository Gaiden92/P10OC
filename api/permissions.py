from django.core.exceptions import ObjectDoesNotExist

from rest_framework import permissions
from rest_framework import generics
from .models import Project

class IsContributorOfProject(permissions.BasePermission):

    def has_permission(self, request, view):
        project = generics.get_object_or_404(Project, pk=view.get('project_pk'))
        print(project)
        if request.method in permissions.SAFE_METHODS:
            return True if request.user in project.contributors else False


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Vérifie si l'utilisateur est l'auteur de l'objet
        return obj.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Autoriser les requêtes GET, HEAD ou OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Autoriser les requêtes POST, PUT, PATCH ou DELETE seulement pour les auteurs du projet
        project_pk = request.data.get('project', None)
        if project_pk:
            project = Project.objects.get(pk=project_pk)
            return project.author == request.user

        return False

    def has_object_permission(self, request, view, obj):
        # Seul l'auteur du projet peut effectuer des opérations sur les contributeurs
        return obj.project.author == request.user

