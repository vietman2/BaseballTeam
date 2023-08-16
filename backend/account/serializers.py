from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ValidationError


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        if not (username and password):
            raise ValidationError({"detail": "[password, username] fields missing."})
        return attrs


from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"