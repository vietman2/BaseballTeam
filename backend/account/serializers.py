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

'''
class ChangePasswordSerializer(ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ["old_password", "new_password"]

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("기존 비밀번호가 일치하지 않습니다")
        return value
    
    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("비밀번호는 8자 이상이어야 합니다")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
'''

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name", "phone_number", "major", "grade", "position"]
