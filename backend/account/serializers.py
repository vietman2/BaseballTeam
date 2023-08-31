from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from .models import UserProfile,CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "phone_number"]

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        phone_number = attrs.get('phone_number','')
        if not (username and password and phone_number):
            raise ValidationError({"detail": "[password, username, phone_number] fields missing."})
        return attrs

class UserAuthorityCheckSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["role"]

class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
