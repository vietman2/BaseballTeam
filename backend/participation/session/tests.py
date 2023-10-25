from django.test import TransactionTestCase
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.apps import apps
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import CustomUser

TrainingType = apps.get_model("session", "TrainingType")

class TrainingTypeAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/trainingtypes/"
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
        self.data = {
            "type": "새 훈련",
            "description": "새 훈련 설명"
        }

    def test_unallowed_methods(self):
        self.client.force_authenticate(user=self.captain_user)
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.get(self.url + "1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_training_types(self):
        self.client.force_authenticate(user=self.captain_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_training_type(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(user=self.captain_user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TrainingType.objects.all().count(), 7)
        self.assertEqual(TrainingType.objects.last().type, self.data['type'])

        self.client.force_authenticate(user=self.normal_user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
