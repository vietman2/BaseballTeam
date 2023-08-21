#### 1
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer,UserProfileSerializer
#### 2
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def generate_token_in_serialized_data(user:User, user_profile:UserProfile) -> UserSerializer.data:
    token = RefreshToken.for_user(user)
    refresh_token, access_token = str(token), str(token.access_token)
    serialized_data = UserProfileSerializer(user_profile).data
    serialized_data['token']={"access":access_token, "refresh":refresh_token}
    return serialized_data  
def set_token_on_response_cookie(user: User) -> Response:
    token = RefreshToken.for_user(user)
    user_profile = UserProfile.objects.get(user=user)
    user_profile_serializer = UserProfileSerializer(user_profile)
    res = Response(user_profile_serializer.data, status=status.HTTP_200_OK)
    res.set_cookie('refresh_token', value=str(token), httponly=True)
    res.set_cookie('access_token', value=str(token.access_token), httponly=True)
    return res
#### view
class SignupView(APIView):
    def post(self, request):
        name=request.data.get('name')
        phone_number=request.data.get('phone_number')
        major=request.data.get('major')
        grade=request.data.get('grade')
        position=request.data.get('position')
        pitcher=request.data.get('pitcher')
    
        user_serialier = UserSerializer(data=request.data)
        if user_serialier.is_valid(raise_exception=True):
            user = user_serialier.save()
            user_profile = UserProfile.objects.create(
            user=user,
            name=name,
            phone_number=phone_number,
            major=major,
            grade=grade,
            position=position,
            pitcher=pitcher
        )
        return set_token_on_response_cookie(user)

class SigninView(APIView):
    def post(self, request):
        try:
            user = User.objects.get(
                username=request.data['username'],
                password=request.data['password'],
                role=request.data['role']

            )
        except:
            return Response({"detail": "아이디 또는 비밀번호를 확인해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        return set_token_on_response_cookie(user)

class LogoutView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "로그인 후 다시 시도해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
        RefreshToken(request.data['refresh']).blacklist()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class TokenRefreshView(APIView):
#     def post(self, request):
#         is_access_token_valid = request.user.is_authenticated
#         refresh_token = request.data['refresh']
#         try:
#             RefreshToken(refresh_token).verify()
#             is_refresh_token_blacklisted = True
#         except:
#             is_refresh_token_blacklisted = False
#         if not is_access_token_valid :  
#             if not is_refresh_token_blacklisted:
#                 return Response({"detail": "login 을 다시 해주세요."}, status=status.HTTP_401_UNAUTHORIZED)
#             else:
#                 new_access_token = str(RefreshToken(refresh_token).access_token)
#         else:
#             user = request.user
#             token = AccessToken.for_user(user)
#             new_access_token = str(token)
#         response = Response({"detail": "token refreshed"}, status=status.HTTP_200_OK)
#         return response.set_cookie('access_token', value=str(new_access_token), httponly=True)

        