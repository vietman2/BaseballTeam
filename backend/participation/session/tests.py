from rest_framework.test import APITestCase

from .models import TrainingType
from account.models import CustomUser

class TrainingTypeAPITestCase(APITestCase):
    def setUp(self):
        TrainingType.objects.create(type="일반", description="일반 훈련")
        TrainingType.objects.create(type="필참-오후", description="필수 참여 오후 훈련 (주로 화요일)")
        TrainingType.objects.create(type="필참-토", description="필수 참여 오전 훈련 (주로 토요일)")
        
        self.normal_user = CustomUser.objects.create_user(
            user_type=CustomUser.UserType.MEMBER,
            name="테스트",
            phone_number="010-1234-5678",
            password="testpw12344321",
            major="컴퓨터공학과",
            grade=3,
            position=CustomUser.Positions.NEW,
        )
        self.captain_user = CustomUser.objects.create_user(
            user_type=CustomUser.UserType.CAPTAIN,
            name="관리자",
            phone_number="010-1234-1234",
            password="testpw12344321",
            major="컴퓨터공학과",
            grade=3,
            position=CustomUser.Positions.NEW,
        )
