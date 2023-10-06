from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from django.utils.datastructures import MultiValueDictKeyError

from .serializers import UserRegisterSerializer, UserProfileSerializer, ChangePasswordSerializer

class RegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try :
            super().post(request, *args, **kwargs)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(None, status=status.HTTP_201_CREATED)

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except MultiValueDictKeyError:
            return Response({"detail": "기존 비밀번호를 입력해주세요"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"detail": "비밀번호가 변경되었습니다"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    serializer_class = UserProfileSerializer
