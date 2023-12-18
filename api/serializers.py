from rest_framework import serializers

from api.models import Project, Issue, Comment, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "id",
            "created_time",
            "user",
            "project"
            ]


class ProjectSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [
            "id",
            "created_time",
            "title",
            "project_type",
            "author",
            "description",
            "contributors"
            ]

    def create(self, validated_data):
        project = Project(**validated_data)
        project.save()
        return project


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model= Issue
        fields = [
            "id",
            "created_time",
            "title",
            "description",
            "project",
            "priority",
            "tag",
            "status",
            "assign_to",
            "author"
            ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "created_time",
            "issue",
            "text",
            "author",
            "link_to_issue",
            "uuid"
            ]