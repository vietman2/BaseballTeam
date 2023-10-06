from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView #, UpdateAPIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserProfileSerializer #, ChangePasswordSerializer

class RegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(None, status=status.HTTP_201_CREATED)

class UserProfileView(APIView):
    serializer_class = UserProfileSerializer
