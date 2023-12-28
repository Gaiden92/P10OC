from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Project, Issue, Comment, Contributor
from api.serializers import ProjectSerializer, IssueSerializer, CommentSerializer, ContributorSerializer
from api.permissions import IsAuthor, IsAuthorOrReadOnly

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve','create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthor]

        return [permission() for permission in permission_classes]


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_queryset(self):
        return Contributor.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    # permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        issues = Issue.objects.filter(project=self.kwargs['project_pk'])
        return issues


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        comments = Comment.objects.filter(issue=self.kwargs['issue_pk'])
        return comments

