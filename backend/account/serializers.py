from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password

from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_type", "name", "phone_number", "major", "grade", "position", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        validate_password(value)

    def create(self, validated_data):
        # user_type and position are not required
        # add them as **extra_fields
        user = CustomUser.objects.create_user(
            **validated_data,
        )

        return user

class ChangePasswordSerializer(ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password"]

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("기존 비밀번호가 일치하지 않습니다")

    def validate_new_password(self, value):
        if value == self.context["request"].data["old_password"]:
            raise serializers.ValidationError("기존 비밀번호와 동일합니다")

        validate_password(value)

    def save(self, **kwargs):
        user = CustomUser.objects.update_password(
            user=self.context["request"].user,
            password=self.context["request"].data["new_password"]
        )
        return user

class UserSimpleSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone_number", "major", "grade", "position"]
