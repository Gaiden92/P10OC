from rest_framework import serializers

from api.models import User, Project

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "age", "can_be_contacted", "can_data_be_shared"]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "created_time", "name", "project_type", "author", "description"]
        