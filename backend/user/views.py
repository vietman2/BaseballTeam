from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from drf_spectacular.utils import extend_schema
from dj_rest_auth.views import LoginView, LogoutView
from django.utils.datastructures import MultiValueDictKeyError
from django.db.utils import IntegrityError

from .serializers import UserRegisterSerializer, UserSchemaSerializer
from .models import CustomUser

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSchemaSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(summary="회원 정보 조회", tags=["회원 관리"])
    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @extend_schema(summary="회원 리스트 조회", tags=["회원 관리"])
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @extend_schema(summary="회원 정보 수정", tags=["회원 관리"])
    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response({"detail": "회원 정보가 수정되었습니다"}, status=status.HTTP_200_OK)
    
    @extend_schema(summary="회원 탈퇴", tags=["회원 관리"])
    def destroy(self, request, *args, **kwargs):
        request.user.delete()
        return Response({"detail": "회원 탈퇴가 완료되었습니다"}, status=status.HTTP_200_OK)

    @extend_schema(
            request=UserRegisterSerializer,
            responses={201: UserSchemaSerializer},
            summary="회원 가입",
            tags=["회원 관리"]
        )
    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.create(serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MyLoginView(LoginView):
    @extend_schema(summary="로그인", tags=["회원 관리"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class MyLogoutView(LogoutView):
    @extend_schema(summary="로그아웃", tags=["회원 관리"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

"""
class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ['put',]

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
"""