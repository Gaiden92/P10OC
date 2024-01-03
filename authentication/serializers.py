from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    """A class represent the serializer of the User object.

    Arguments:
        serializers -- A class ModelSerializer

    Returns:
        None
    """
    class Meta:
        """A meta class of the serializer object. 
        """
        model = User
        fields = [
            "id",
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared"]
        extra_kwargs = {"password": {"write_only": True}}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields.pop('password')

    def create(self, validated_data:tuple)->object:
        """Method for create a User.

        Arguments:
            validated_data -- tuple: Tuple of data

        Returns:
            the user object
        """
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    """A class to represent the user login serializer

    Arguments:
        serializers -- A class Serializer
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

