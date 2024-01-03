from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from authentication.serializers import UserSerializer, UserLoginSerializer
from authentication.models import User
from authentication.permissions import isOwner


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [isOwner]

        return [permission() for permission in permission_classes]


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer
