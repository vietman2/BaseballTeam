from rest_framework.test import APITestCase
from rest_framework import status
from django.core.management import call_command

from .models import CustomUser

class RegisterAPITestCase(APITestCase):
    ## Test cases for registration
    def setUp(self):
        self.data = {
            "user_type": 1,
            "name": "테스트",
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
            "major": "전공없음",
            "grade": 1,
            "position": 0
        }
        self.simple = {
            "name": "테스트",
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
        }
        self.no_phone_number = {
            "name": "테스트",
            "password": "testpassword1234",
        }
        self.no_name = {
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
        }

    def test_registration_success(self):
        self.assertEqual(CustomUser.objects.count(), 0)

        response = self.client.post("/api/account/register/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        created_user = CustomUser.objects.get(phone_number="010-1234-5678")
        self.assertEqual(created_user.user_type, 1)
        self.assertEqual(created_user.name, "테스트")
        self.assertEqual(created_user.major, "전공없음")
        self.assertEqual(created_user.grade, 1)
        self.assertEqual(created_user.position, 0)
        self.assertFalse(created_user.is_superuser)

        ## 비밀번호가 암호화되었는지 확인
        self.assertNotEqual(created_user.password, "testpassword1234")

    def test_registration_success_default_fields(self):
        response = self.client.post("/api/account/register/", data=self.simple)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        created_user = CustomUser.objects.get(phone_number="010-1234-5678")
        self.assertEqual(created_user.user_type, 0)
        self.assertEqual(created_user.major, "전공없음")
        self.assertEqual(created_user.grade, 1)
        self.assertEqual(created_user.position, 0)

    def test_registration_success_superuser(self):
        call_command(
            "createsuperuser",
            name="admin",
            phone_number="010-1234-4321",
            interactive=False
        )

        created_user = CustomUser.objects.get(phone_number="010-1234-4321")
        self.assertEqual(created_user.user_type, 1)
        self.assertTrue(created_user.is_superuser)

    def test_registration_fail(self):
        ## 잘못된 전화번호 형식.
        self.data["phone_number"] = "010-1234-56789"
        response = self.client.post("/api/account/register/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="010-1234-56789").exists())

        self.data["phone_number"] = "01012345678"
        response = self.client.post("/api/account/register/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="01012345678").exists())

        self.data["phone_number"] = "010 1234 1234"
        response = self.client.post("/api/account/register/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="010 1234 1234").exists())

        ## 정보 누락
        response = self.client.post("/api/account/register/", data=self.no_phone_number)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        ## check ValueError
        self.assertFalse(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        response = self.client.post("/api/account/register/", data=self.no_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPITestCase(APITestCase):
    ## Test cases for changing password
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            user_type=1,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.success_data = {
            "user": self.user,
            "old_password": "testpassword1234",
            "new_password": "newpassword1234"
        }
        self.wrong_old_password = {
            "user": self.user,
            "old_password": "wrongpassword1234",
            "new_password": "newpassword1234"
        }
        self.no_old_password = {
            "user": self.user,
            "new_password": "newpassword1234"
        }
        self.same_password = {
            "user": self.user,
            "old_password": "testpassword1234",
            "new_password": "testpassword1234"
        }
        self.no_new_password = {
            "user": self.user,
            "old_password": "testpassword1234"
        }

    def test_change_password_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/api/account/change-password/", data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newpassword1234"))

    def test_change_password_fail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/api/account/change-password/", data=self.wrong_old_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put("/api/account/change-password/", data=self.no_old_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put("/api/account/change-password/", data=self.same_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put("/api/account/change-password/", data=self.no_new_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
