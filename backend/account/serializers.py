from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from .models import CustomUser

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
    class Meta:
        model = CustomUser
        fields = ["is_pitcher", "is_active", "position", "grade", "major", "name"]
