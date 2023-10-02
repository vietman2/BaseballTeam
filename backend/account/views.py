from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import UserSerializer,UserProfileSerializer


def set_token_on_response_cookie(user: CustomUser) -> Response:
    token = RefreshToken.for_user(user)
    user_profile = CustomUser.objects.get(user=user)
    user_profile_serializer = UserProfileSerializer(user_profile)
    res = Response(user_profile_serializer.data, status=status.HTTP_200_OK)
    res.set_cookie('refresh_token', value=str(token), httponly=True)
    res.set_cookie('access_token', value=str(token.access_token), httponly=True)
    return res

class SignupStep1View(APIView):
    def post(self,request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()  # 실제 데이터베이스에 사용자를 저장
        return Response({"user_id" : user.id}, status = status.HTTP_200_OK)

class SignupStep2View(APIView):
    def post(self,request):
        userprofile_serializer = UserProfileSerializer(request.user, data =request.data)
        if userprofile_serializer.is_valid():
            userprofile_serializer.save()
        return set_token_on_response_cookie(request.user)

class SigninView(APIView):
    def post(self,request):
        try:
            user = CustomUser.objects.get(
                username=request.data['username'],
                password=request.data['password']
            )
        except CustomUser.DoesNotExist:
            return Response({"detail": "아이디 또는 비밀번호를 확인해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        return set_token_on_response_cookie(user)

class LogoutView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        RefreshToken(request.data['refresh']).blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)
