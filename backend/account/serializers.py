from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_type", "name", "phone_number", "major", "grade", "position", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def validate_phone_number(self, attrs):
        if attrs["user_type"] == 1:
            raise ValidationError("관리자는 직접 생성할 수 없습니다")
        ## 클라이언트에서 전화번호가 - 없이 010xxxxyyyy 형태로 들어오면
        ## 여기서 -를 붙여주도록 구현
        phone_number = attrs["phone_number"]
        if phone_number.find("-") == -1:
            attrs["phone_number"] = phone_number[:3] + "-" + phone_number[3:7]
            attrs["phone_number"] = attrs["phone_number"] + "-" + phone_number[7:]

        return attrs

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True}}

class UserPasswordChangeSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["password"]
        extra_kwargs = {"password": {"write_only": True}}

class UserAuthorityCheckSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_type"]

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone_number", "major", "grade", "position"]
