from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_type", "name", "phone_number", "major", "grade", "position", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            user_type=validated_data["user_type"],
            name=validated_data["name"],
            phone_number=validated_data["phone_number"],
            major=validated_data["major"],
            grade=validated_data["grade"],
            position=validated_data["position"],
            password=validated_data["password"]
        )
        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone_number", "major", "grade", "position"]
