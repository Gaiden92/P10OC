from django.shortcuts import get_object_or_404
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
        fields = '__all__'
        extra_fields = 'contributors'
        read_only_fields = ["author"]

    def create(self, validated_data):
        project = Project(**validated_data)
        project.save()
        contributor = Contributor(user=project.author, project=project)
        contributor.save()

        return project


class IssueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Issue
        fields = "__all__"
        read_only_fields  = ["author"]


    def create(self, validated_data):
        issue = Issue(**validated_data)
        project_pk = self.context.get('view').kwargs.get('project_pk')
        issue.project = project_pk
        issue.save()
  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["title", "author", "link_to_issue", "issue"]
