from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from drf_spectacular.utils import extend_schema
from dj_rest_auth.views import LoginView, LogoutView

from .serializers import UserRegisterSerializer, UserProfileSerializer, PasswordChangeSerializer
from .models import CustomUser
from .permissions import IsSelf

class UserViewSet(ModelViewSet):
    queryset = CustomUser.active_members.get_queryset()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options', 'trace']

    @extend_schema(exclude=True)
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(summary="회원 정보 조회", tags=["회원 관리"])
    def retrieve(self, request, *args, **kwargs):
        if not IsSelf().has_object_permission(request, self, kwargs["pk"]):
            return Response({"detail": "잘못된 요청입니다"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @extend_schema(summary="회원 리스트 조회", tags=["회원 관리"])
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @extend_schema(summary="회원 정보 수정", tags=["회원 관리"])
    def partial_update(self, request, *args, **kwargs):
        if not IsSelf().has_object_permission(request, self, kwargs["pk"]):
            return Response({"detail": "잘못된 요청입니다"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "회원 정보가 수정되었습니다"}, status=status.HTTP_200_OK)

    @extend_schema(summary="회원 탈퇴", tags=["회원 관리"])
    def destroy(self, request, *args, **kwargs):
        if not IsSelf().has_object_permission(request, self, kwargs["pk"]):
            return Response({"detail": "잘못된 요청입니다"}, status=status.HTTP_400_BAD_REQUEST)

        CustomUser.objects.delete_user(request.user)
        return Response({"detail": "회원 탈퇴가 완료되었습니다"}, status=status.HTTP_200_OK)

    @extend_schema(
            request=UserRegisterSerializer,
            responses={201: UserProfileSerializer},
            summary="회원 가입",
            tags=["회원 관리"]
        )
    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny],
        serializer_class=UserRegisterSerializer
    )
    def register(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.validate_passwords(serializer.validated_data)
            serializer.save()
            headers = self.get_success_headers(serializer.data)
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @extend_schema(summary="비밀번호 변경", tags=["회원 관리"])
    @action(detail=False, methods=["patch"], serializer_class=PasswordChangeSerializer)
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "비밀번호가 변경되었습니다"}, status=status.HTTP_200_OK)

class MyLoginView(LoginView):
    @extend_schema(summary="로그인", tags=["회원 관리"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MyLogoutView(LogoutView):
    serializer_class = None
    http_method_names = ['post', 'head', 'options', 'trace']

    @extend_schema(summary="로그아웃", tags=["회원 관리"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
