from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from authentication.serializers import UserSerializer, UserLoginSerializer
from authentication.models import User
from authentication.permissions import isOwner


class UserViewSet(ModelViewSet):
    """A class represent the User model viewset.

    Arguments:
        ModelViewSet -- A ModelViewSet class

    Returns:
        None
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        """Method to get data for the view.

        Returns:
            Queryset
        """
        return User.objects.all()

    def get_permissions(self):
        """Method to get the permissions of the view.

        Returns:
            list
        """
        if self.action in ["list"]:
            permission_classes = [IsAuthenticated]
        elif self.action in ["create"]:
            permission_classes = [AllowAny]
        
        else:
            permission_classes = [IsAuthenticated & isOwner]

        return [permission() for permission in permission_classes]


class UserLoginAPIView(TokenObtainPairView):
    """A class that represents the user login view

    Arguments:
        TokenObtainPairView -- class
    """

    serializer_class = UserLoginSerializer
