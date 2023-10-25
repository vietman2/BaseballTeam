from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import SetPasswordForm

from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "phone_number",
            "freshman_year",
            "major",
            "grade",
            "position",
            "password",
            "password2"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def validate_passwords(self, value):
        if value["password"] != value["password2"]:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다")

        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        validated_data.pop("password2")
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def save(self, **kwargs):
        self.create(self.validated_data)
        return self.validated_data

class PasswordChangeSerializer(ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password1 = serializers.CharField(required=True, write_only=True)
    new_password2 = serializers.CharField(required=True, write_only=True)

    set_password_form_class = SetPasswordForm
    set_password_form = None

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password1", "new_password2"]
        extra_kwargs = {
            "old_password": {"write_only": True},
            "new_password1": {"write_only": True},
            "new_password2": {"write_only": True}
        }

    def validate(self, attrs):
        if attrs["new_password1"] != attrs["new_password2"]:
            raise serializers.ValidationError("새로운 비밀번호가 일치하지 않습니다")

        if attrs["old_password"] == attrs["new_password1"]:
            raise serializers.ValidationError("새로운 비밀번호가 기존 비밀번호와 일치합니다")

        if not self.context["request"].user.check_password(attrs["old_password"]):
            raise serializers.ValidationError("기존 비밀번호가 일치하지 않습니다")

        self.set_password_form = self.set_password_form_class(
            user=self.context["request"].user,
            data=attrs
        )

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)

        return attrs

    def save(self, **kwargs):
        self.set_password_form.save()
        self.set_password_form.user.refresh_from_db()
        return self.set_password_form.user

class UserProfileSerializer(ModelSerializer):
    phone_number = serializers.CharField(required=False)
    freshman_year = serializers.IntegerField(required=False)

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "phone_number",
            "freshman_year",
            "major",
            "grade",
            "position",
        ]

class HandoverSerializer(ModelSerializer):
    old_captain = serializers.ModelField(
        model_field=CustomUser._meta.get_field("phone_number")
    )
    new_captain = serializers.ModelField(
        model_field=CustomUser._meta.get_field("phone_number")
    )
    old_vice_captain = serializers.ModelField(
        model_field=CustomUser._meta.get_field("phone_number")
    )
    new_vice_captain = serializers.ModelField(
        model_field=CustomUser._meta.get_field("phone_number")
    )

    class Meta:
        model = CustomUser
        fields = ["old_captain", "new_captain", "old_vice_captain", "new_vice_captain"]\
        
    def validate_old_captain(self, value):
        if not CustomUser.objects.filter(phone_number=value, user_type=CustomUser.UserType.CAPTAIN).exists():
            raise serializers.ValidationError("주장이 아닙니다")

        return value
    
    def validate_new_captain(self, value):
        if not CustomUser.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("전화번호가 존재하지 않습니다")

        return value
    
    def validate_old_vice_captain(self, value):
        if not CustomUser.objects.filter(phone_number=value, user_type=CustomUser.UserType.VICE_CAPTAIN).exists():
            raise serializers.ValidationError("부주장이 아닙니다")

        return value
    
    def validate_new_vice_captain(self, value):
        if not CustomUser.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("전화번호가 존재하지 않습니다")

        return value

    def save(self, **kwargs):
        CustomUser.objects.handover_leadership(self.validated_data)
        return self.validated_data

class UserManagementSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "name",
            "phone_number",
            "freshman_year",
            "major",
            "grade",
            "position",
            "user_type",
            "date_joined",
            "last_login",
            "is_active",
        ]

class StatusChangeSerializer(ModelSerializer):
    new_status = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ["phone_number", "new_status"]

    def validate_new_status(self, value):
        if value not in CustomUser.UserType.names:
            raise serializers.ValidationError("유저 유형이 올바르지 않습니다")
        
        return value
    
    def validate_phone_number(self, value):
        if not CustomUser.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("전화번호가 존재하지 않습니다")

        return value

    def save(self, **kwargs):
        CustomUser.objects.change_user_type(self.validated_data)
        return self.validated_data
