from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser
from .serializers import UserProfileSerializer

def set_token_on_response_cookie(user: CustomUser) -> Response:
    ## TODO: 쿠키는 그렇다 치고, 세션은?
    token = RefreshToken.for_user(user)
    user_profile = CustomUser.objects.get(user=user)
    user_profile_serializer = UserProfileSerializer(user_profile)
    res = Response(user_profile_serializer.data, status=status.HTTP_200_OK)
    res.set_cookie('refresh_token', value=str(token), httponly=True)
    res.set_cookie('access_token', value=str(token.access_token), httponly=True)
    return res

class SignupView(APIView):
    def post(self,request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create()
            return Response({"detail": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return set_token_on_response_cookie(serializer.user)

class SigninView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            return set_token_on_response_cookie(serializer.user)
        return Response({"detail": "로그인에 실패했습니다."}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        res = Response({"detail": "로그아웃되었습니다."}, status=status.HTTP_200_OK)
        res.delete_cookie('refresh_token')
        res.delete_cookie('access_token')
        return res

class PasswordChangeView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update_password()
            return Response({"detail": "비밀번호가 변경되었습니다."}, status=status.HTTP_200_OK)
        return Response({"detail": "비밀번호 변경에 실패했습니다."}, status=status.HTTP_400_BAD_REQUEST)

class AuthorityCheckView(APIView):
    def get(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"detail": "권한이 확인되었습니다."}, status=status.HTTP_200_OK)
        return Response({"detail": "권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
