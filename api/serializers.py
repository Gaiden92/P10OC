from rest_framework import serializers

from api.models import User, Project, Issue, Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id",
        "created_time",
        "username",
        "age",
        "can_be_contacted",
        "can_data_be_shared"
        ]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "created_time",
            "title",
            "project_type",
            "author",
            "description"
            ]
        
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