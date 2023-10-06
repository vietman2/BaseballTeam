from rest_framework.serializers import ModelSerializer

from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_type", "name", "phone_number", "major", "grade", "position", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # user_type and position are not required
        # add them as **extra_fields
        user = CustomUser.objects.create_user(
            **validated_data,
        )

        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone_number", "major", "grade", "position"]
