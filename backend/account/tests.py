from rest_framework.test import APITestCase
from rest_framework import status

from .models import CustomUser

class RegisterAPITestCase(APITestCase):
    ## Test cases for registration
    def test_registration(self):
        ## 성공
        ## 응답코드 201
        ## DB에 저장

        data = {
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
            "user_type": 1,
            "name": "테스트",
            "major": "전공없음",
            "grade": 1,
            "position": 0
        }
        response = self.client.post("/api/account/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        created_user = CustomUser.objects.get(phone_number="010-1234-5678")
        self.assertEqual(created_user.user_type, 1)
        self.assertEqual(created_user.name, "테스트")
        self.assertEqual(created_user.major, "전공없음")
        self.assertEqual(created_user.grade, 1)
        self.assertEqual(created_user.position, 0)


        ## 실패
        ## 응답코드 400
        ## DB에 저장되지 않음

        data = {
            "phone_number": "010-1234-56789",
            "password": "testpassword1234",
            "user_type": "NEW_ACCOUNT",
            "name": "테스트",
            "major": "전공없음",
            "grade": 1,
            "position": 0
        }
        response = self.client.post("/api/account/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="010-1234-56789").exists())

