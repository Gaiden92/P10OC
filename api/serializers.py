from rest_framework import serializers

from api.models import Project, Issue, Comment, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    """A class representation of a contributor serializer.

    Arguments:
        serializers -- class ModelSerializer
    """
    class Meta:
        model = Contributor
        fields = [
            "id",
            "created_time",
            "user",
            "project"
            ]


class ProjectSerializer(serializers.ModelSerializer):
    """A class representation of a contributor serializer.

    Arguments:
        serializers -- class ModelSerializer
    Returns:
        None
    """
    contributors = ContributorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        extra_fields = 'contributors'
        read_only_fields = ["author", "id"]

    def create(self, validated_data: list) -> object:
        """Method to create a project instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a project object
        """
        request = self.context.get('request', None)
        if request:
            user = request.user
        project = Project(
            title=validated_data["title"],
            description=validated_data['description'],
            project_type=validated_data['project_type'],
            author=user
        )

        project.save()
        contributor = Contributor(user=project.author, project=project)
        contributor.save()

        return project


class IssueSerializer(serializers.ModelSerializer):
    """A class representation of a issue serializer.

    Arguments:
        serializers -- class ModelSerializer
    """
    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = ["author", "id"]

    def create(self, validated_data: list) -> object:
        """Method to create a issue instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a issue object
        """
        project = Project.objects.get(
            id=self.context['view'].kwargs['project_pk']
            )
        request = self.context.get('request', None)
        if request:
            user = request.user
        issue = Issue.objects.create(
            assign_to=validated_data["assign_to"],
            project=project,
            title=validated_data["title"],
            description=validated_data["description"],
            tag=validated_data["tag"],
            priority=validated_data["priority"],
            status=validated_data['status'],
            author=user
        )

        return issue


class CommentSerializer(serializers.ModelSerializer):
    """A class representation of a comment serializer.

    Arguments:
        serializers -- class ModelSerializer
    """
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data: list) -> object:
        """Method to create a comment instance.

        Arguments:
            validated_data -- list: data

        Returns:
            obj: a comment object
        """
        issue = Issue.objects.get(id=self.context['view'].kwargs['issue_pk'])
        request = self.context.get('request', None)
        if request:
            user = request.user
        comment = Comment.objects.create(
            text=validated_data['text'],
            issue=issue,
            author=user
        )

        return comment
