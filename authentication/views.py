from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import UserLoginSerializer, JWTTokenSerializer
from authentication.serializers import UserSerializer, UserLoginSerializer, JWTTokenSerializer
from authentication.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class UserLoginAPIView(TokenObtainPairView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == status.HTTP_200_OK:
            user = self.serializer_class.get_user(response.data)
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            response.data.update({
                'refresh': str(refresh),
                'access': str(access_token),
            })

        return response

class UserTokenRefreshAPIView(TokenRefreshView):
    serializer_class = JWTTokenSerializer