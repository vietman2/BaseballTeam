from rest_framework.test import APITestCase

from .models import TrainingType
from user.models import CustomUser

"""
class TrainingTypeAPITestCase(APITestCase):
    def setUp(self):        
        self.normal_user = CustomUser.objects.create_user(
            user_type=CustomUser.UserType.MEMBER,
            name="테스트",
            phone_number="010-1234-5678",
            password="testpw12344321",
            freshman_year=2019,
            major="컴퓨터공학과",
            grade=3,
            position=CustomUser.Positions.NEW,
        )
        self.captain_user = CustomUser.objects.create_user(
            user_type=CustomUser.UserType.CAPTAIN,
            name="관리자",
            phone_number="010-1234-1234",
            password="testpw12344321",
            freshman_year=2019,
            major="컴퓨터공학과",
            grade=3,
            position=CustomUser.Positions.NEW,
        )

    def test_unallowed_methods(self):
        self.client.force_authenticate(user=self.captain_user)
        response = self.client.put('/api/participation/session/trainingtypes/')
        self.assertEqual(response.status_code, 405)
        response = self.client.delete('/api/participation/session/trainingtypes/')
        self.assertEqual(response.status_code, 405)
        response = self.client.patch('/api/participation/session/trainingtypes/')
        self.assertEqual(response.status_code, 405)

    def test_get_list_normal_user(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get('/api/participation/session/trainingtypes/')
        self.assertEqual(response.status_code, 403)

    def test_get_list_captain_user(self):
        self.client.force_authenticate(user=self.captain_user)
        response = self.client.get('/api/participation/session/trainingtypes/')
        self.assertEqual(response.status_code, 200)
"""