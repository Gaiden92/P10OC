from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.models import Project, Issue, Comment, Contributor
from api.serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
    ContributorSerializer,
)
from api.permissions import (
    IsAuthor,
    IsAuthorOrReadOnly,
    IsContributor,
    IsContributorForIssue,
    IsAuthorOfIssue,
    IsContributorForComment,
    IsAuthorOfComment,
)


class ProjectViewSet(ModelViewSet):
    """A class representation of a project.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = ProjectSerializer

    def get_queryset(self) -> object:
        """Method to get all the project of the database.

        Returns:
            object: queryset containing all projects
        """
        return Project.objects.all()

    def get_permissions(self) -> list:
        """Method to give permission to user

        Returns:
            list
        """
        if self.action in ["create"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["list", "retrieve"]:
            permission_classes = [
                IsAuthenticated,
                IsContributor | IsAuthor,
            ]
        else:
            permission_classes = [IsAuthor]
        return [permission() for permission in permission_classes]


class ContributorViewSet(ModelViewSet):
    """A class representation of a contributor.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self) -> object:
        """Method to get all the project's contributors.

        Returns:
            object: queryset containing all contributors
        """
        contributors = Contributor.objects.filter(
            project=self.kwargs["project_pk"]
            )
        return contributors


class IssueViewSet(ModelViewSet):
    """A class representation of a issue.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = IssueSerializer

    def get_permissions(self) -> list:
        """Method to give permission to user

        Returns:
            list
        """
        if self.action in ["list", "retrieve", "create"]:
            permission_classes = [
                IsAuthenticated & IsContributorForIssue,
            ]
        else:
            permission_classes = [IsAuthorOfIssue]

        return [permission() for permission in permission_classes]

    def get_queryset(self) -> object:
        """Method to get all the project's issues.

        Returns:
            object: queryset containing all issues
        """
        issues = Issue.objects.filter(project=self.kwargs["project_pk"])
        return issues


class CommentViewSet(ModelViewSet):
    """A class representation of a comment.

    Arguments:
        ModelViewSet -- class ModelViewSet

    Returns:
        None
    """

    serializer_class = CommentSerializer

    def get_queryset(self) -> object:
        """Method to get all the issue's comments.

        Returns:
            object: queryset containing all comments
        """
        comments = Comment.objects.filter(issue=self.kwargs["issue_pk"])
        return comments

    def get_permissions(self) -> list:
        """Method to give permission to user

        Returns:
            list
        """
        if self.action in ["list", "retrieve", "create"]:
            permission_classes = [
                IsAuthenticated & IsContributorForComment,
            ]
        else:
            permission_classes = [IsAuthenticated & IsAuthorOfComment]

        return [permission() for permission in permission_classes]
