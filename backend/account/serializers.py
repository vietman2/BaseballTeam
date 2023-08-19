from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password","role"]

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        role = attrs.get('role','')
        if not (username and password and role):
            raise ValidationError({"detail": "[password, username, role] fields missing."})
        return attrs


from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"