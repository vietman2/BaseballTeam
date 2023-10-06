from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserProfileSerializer #, ChangePasswordSerializer

class RegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(None, status=status.HTTP_201_CREATED)

"""
class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "비밀번호가 변경되었습니다"}, status=status.HTTP_200_OK)
"""

class UserProfileView(APIView):
    serializer_class = UserProfileSerializer
