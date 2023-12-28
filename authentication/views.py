from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import AllowAny, IsAuthenticated
from authentication.serializers import UserSerializer, UserLoginSerializer
from authentication.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

from rest_framework_simplejwt.views import TokenObtainPairView

class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer 
