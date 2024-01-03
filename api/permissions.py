from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from .models import Project, Contributor


class IsAuthor(permissions.BasePermission):
    """A class that reprensents a permission to check if the current
    user is the author of the project.

    Arguments:
        permissions -- a class BasePermission
    """

    def has_object_permission(
            self,
            request: str,
            view: object,
            obj: object
    ) -> bool:
        """Method to check if the current
        user is the author of the project.

        Arguments:
            request -- str: a request
            view -- obj: a view
            obj -- obj: an object

        Returns:
            bool
        """
        return obj.author == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is the author of the project.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_permission(
            self,
            request: str,
            view: object
    ) -> bool:
        """A method to check if current user
        is the author of the project.

        Arguments:
            request -- str: a request
            view -- obj: a view

        Returns:
            bool
        """
        if request.method in permissions.SAFE_METHODS \
                and request.user.is_authenticated:
            return True

        project_pk = request.data.get("project", None)
        if project_pk:
            project = Project.objects.get(pk=project_pk)
            return project.author == request.user

        return False

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is the author of the project.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """

        return obj.project.author == request.user


class IsContributor(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is a project's contributor.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        contributors = Contributor.objects.filter(project=obj)
        return contributors.filter(user=request.user)


class IsContributorForIssue(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_permission(self, request: str, view: object):
        """A method to check if current user
        is a project's contributor.

        Arguments:
            request -- str: a request
            view -- obj: a view

        Returns:
            bool
        """
        if view.action in ["list", "retrieve"]:
            try:
                project = Project.objects.get(id=view.kwargs["project_pk"])
            except ObjectDoesNotExist:
                return False
            return project.contributors.filter(user=request.user)

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is a project's contributor.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        contributors = Contributor.objects.filter(project=obj.project)
        return contributors.filter(user=request.user)


class IsAuthorOfIssue(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is the author of the issue.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is the author of the issue.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        return obj.author == request.user


class IsContributorForComment(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is a project's contributor.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_permission(self, request: str, view: object):
        """A method to check if current user
        is a project's contributor.

        Arguments:
            request -- str: a request
            view -- obj: a view

        Returns:
            bool
        """
        if view.action in ["list", "retrieve"]:
            try:
                project = Project.objects.get(id=view.kwargs["project_pk"])
            except ObjectDoesNotExist:
                return False
            return project.contributors.filter(user=request.user)

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is a project's contributor.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        contributors = Contributor.objects.filter(project=obj.issue.project)
        return contributors.filter(user=request.user)


class IsAuthorOfComment(permissions.BasePermission):
    """A class that represents a permission to check if current user
        is the author of the comment.

    Arguments:
        permissions -- A class BasePermission
    """

    def has_object_permission(self, request: str, view: object, obj: object):
        """Method to check if the current
        user is the author of the comment.

        Arguments:
            request -- str: a request
            view -- str: a view
            obj -- object: an object

        Returns:
            bool
        """
        return obj.author == request.user
