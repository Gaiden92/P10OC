from rest_framework import permissions
from .models import Project


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Vérifie si l'utilisateur est un contributeur au projet
            if request.user in obj.contributors:
                return True
            else:
                return False
        # Vérifie si l'utilisateur est l'auteur de l'objet
        return obj.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Autoriser les requêtes GET, HEAD ou OPTIONS
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
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

