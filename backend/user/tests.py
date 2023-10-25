from rest_framework.test import APITestCase
from rest_framework import status
from django.core.management import call_command

from .models import CustomUser

class RegisterAPITestCase(APITestCase):
    ## Test cases for registration
    def setUp(self):
        self.url = "/api/users/register/"
        self.data = {
            "name": "테스트",
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
            "password2": "testpassword1234",
            "freshman_year": 2019,
            "major": "전공없음",
            "grade": 1,
            "position": 0
        }
        self.simple = {
            "name": "테스트",
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
            "password2": "testpassword1234",
            "freshman_year": 2019,
        }
        self.no_phone_number = {
            "name": "테스트",
            "password": "testpassword1234",
        }
        self.no_name = {
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
        }
        self.no_password2 = {
            "name": "테스트",
            "phone_number": "010-1234-5678",
            "password": "testpassword1234",
        }

    def test_unallowed_methods(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_registration_success(self):
        self.assertEqual(CustomUser.objects.count(), 0)

        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        ## 디폴트 값 확인
        created_user = CustomUser.objects.get(phone_number="010-1234-5678")
        self.assertEqual(created_user.user_type, 0)
        self.assertEqual(created_user.name, "테스트")
        self.assertEqual(created_user.major, "전공없음")
        self.assertEqual(created_user.grade, 1)
        self.assertEqual(created_user.position, 0)
        self.assertFalse(created_user.is_superuser)

        ## 비밀번호가 암호화되었는지 확인
        self.assertNotEqual(created_user.password, "testpassword1234")

    def test_registration_success_superuser(self):
        call_command(
            "createsuperuser",
            name="admin",
            phone_number="010-1234-4321",
            freshman_year=2015,
            interactive=False
        )

        created_user = CustomUser.objects.get(phone_number="010-1234-4321")
        self.assertEqual(created_user.user_type, 1)
        self.assertTrue(created_user.is_superuser)

    def test_registration_fail_unique(self):
        ## 이미 존재하는 전화번호
        self.client.post(self.url, data=self.data)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_registration_fail_password(self):
        # 1. 비밀번호가 8자리 이하
        self.data["password"] = "test123"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 2. 비밀번호가 너무 쉬움
        self.data["password"] = "password"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 3. 비밀번호가 숫자로만 이루어짐
        self.data["password"] = "12345678"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 4. 비밀번호 확인이 일치하지 않음
        self.data["password"] = "testpassword1234"
        self.data["password2"] = "wrongpassword1234"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_fail(self):
        ## 잘못된 전화번호 형식.
        self.data["phone_number"] = "010-1234-56789"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="010-1234-56789").exists())

        self.data["phone_number"] = "01012345678"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="01012345678").exists())

        self.data["phone_number"] = "010 1234 1234"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(CustomUser.objects.filter(phone_number="010 1234 1234").exists())

        ## 정보 누락
        response = self.client.post(self.url, data=self.no_phone_number)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        ## check ValueError
        self.assertFalse(CustomUser.objects.filter(phone_number="010-1234-5678").exists())

        response = self.client.post(self.url, data=self.no_name)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/login/"
        self.user = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            freshman_year=2019,
            user_type=1,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.data = {
            "username": "010-1234-5678",
            "password": "testpassword1234"
        }
        self.wrong_password = {
            "username": "010-1234-5678",
            "password": "wrongpassword1234"
        }
        self.no_password = {
            "username": "010-1234-5678"
        }
        self.no_phone_number = {
            "username": "testpassword1234"
        }

    def test_unallowed_methods(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_login_success(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        ## 로그인 성공 시, 토큰이 발급되었는지 확인
        self.assertTrue("access" in response.data)
        self.assertTrue("refresh" in response.data)

    def test_login_fail(self):
        response = self.client.post(self.url, data=self.wrong_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(self.url, data=self.no_password)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(self.url, data=self.no_phone_number)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(self.url, data={"username": "010-1234-4321"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        ## user not active
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LogoutAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/logout/"
        self.user = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            freshman_year=2019,
            user_type=1,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.data = {
            "username": "010-1234-5678",
            "password": "testpassword1234"
        }

    def test_unallowed_methods(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_logout_success(self):
        response = self.client.post("/api/login/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data["access"]
        refresh_token = response.data["refresh"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.post(self.url, data={"refresh": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logoout_fail(self):
        response = self.client.post("/api/login/", data=self.data)

        ## refresh token이 없을 때
        response = self.client.post(self.url, data={})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        ## refresh token이 잘못되었을 때
        response = self.client.post(self.url, data={"refresh": "wrongtoken"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ChangePasswordAPITestCase(APITestCase):
    ## Test cases for changing password
    def setUp(self):
        self.url = "/api/users/change_password/"
        self.user = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            freshman_year=2019,
            user_type=1,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.success_data = {
            "user": self.user,
            "old_password": "testpassword1234",
            "new_password1": "newpassword1234",
            "new_password2": "newpassword1234"
        }

    def test_unallowed_methods(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_change_password_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password("newpassword1234"))

    def test_change_password_fail(self):
        self.client.force_authenticate(user=self.user)

        # 1. old password가 틀린 경우
        self.success_data["old_password"] = "wrongpassword1234"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 2. old password와 new password가 같은 경우
        self.success_data["old_password"] = "testpassword1234"
        self.success_data["new_password1"] = "testpassword1234"
        self.success_data["new_password2"] = "testpassword1234"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 3. new password 1과 new password 2가 다른 경우
        self.success_data["new_password1"] = "newpassword1234"
        self.success_data["new_password2"] = "wrongpassword1234"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 4. new password가 8자리 이하
        self.success_data["new_password1"] = "new123"
        self.success_data["new_password2"] = "new123"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 5. new password가 너무 쉬움
        self.success_data["new_password1"] = "password"
        self.success_data["new_password2"] = "password"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 6. new password가 숫자로만 이루어짐
        self.success_data["new_password1"] = "12345678"
        self.success_data["new_password2"] = "12345678"
        response = self.client.patch(self.url, data=self.success_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 7. empty fields
        response = self.client.patch(self.url, data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteAccountAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/users/1/"
        self.user = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            freshman_year=2019,
            user_type=1,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.user2 = CustomUser.objects.create_user(
            phone_number="010-1234-4321",
            password="testpassword1234",
            freshman_year=2019,
            user_type=3,
            name="테스트2",
            major="전공없음",
            grade=1,
            position=0
        )

    def test_delete_success(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user.refresh_from_db()
        user = CustomUser.objects.get(phone_number="010-1234-5678")
        self.assertFalse(user.is_active)

    def test_delete_fail(self):
        # not logged in
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # wrong user
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/api/users/2/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # not exist
        response = self.client.delete("/api/users/3/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="testpassword1234",
            freshman_year=2019,
            user_type=4,
            name="테스트",
            major="전공없음",
            grade=1,
            position=0
        )
        self.user2 = CustomUser.objects.create_user(
            phone_number="010-1234-4321",
            password="testpassword1234",
            freshman_year=2019,
            user_type=3,
            name="테스트2",
            major="전공없음",
            grade=1,
            position=0
        )
        self.inactive_user = CustomUser.objects.create_user(
            phone_number="010-1234-1234",
            password="testpassword1234",
            freshman_year=2019,
            user_type=7,
            name="테스트3",
            major="전공없음",
            grade=1,
            position=0
        )
        self.data = {
            "name": "바뀐이름",
        }

    def test_unallowed_method(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_success(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_fail(self):
        # not logged in
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_success(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/users/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_fail(self):
        # not logged in
        response = self.client.get("/api/users/1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # wrong user
        self.client.force_authenticate(user=self.user1)
        response = self.client.get("/api/users/2/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # not exist
        response = self.client.get("/api/users/3/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_success(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch("/api/users/1/", data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.user1.refresh_from_db()
        self.assertEqual(self.user1.name, "바뀐이름")

    def test_partial_update_fail(self):
        # not logged in
        response = self.client.patch("/api/users/1/", data={"name": "테스트2"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # wrong user
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch("/api/users/2/", data={"name": "테스트2"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # not exist
        response = self.client.patch("/api/users/3/", data={"name": "테스트2"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # validation error
        response = self.client.patch("/api/users/1/", data={"name": ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class HandoverAPITestCase(APITestCase):
    def setUp(self):
        self.old_captain = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="oldcaptain1234",
            freshman_year=2018,
            user_type=2,
            name="기존주장",
            major="체육교육과",
            grade=4,
            position=3
        )
        self.new_captain = CustomUser.objects.create_user(
            phone_number="010-1234-4321",
            password="newcaptain1234",
            freshman_year=2019,
            user_type=5,
            name="새로운주장",
            major="수학교육과",
            grade=3,
            position=6
        )
        self.old_vice_captain = CustomUser.objects.create_user(
            phone_number="010-1234-1234",
            password="oldvicecaptain1234",
            freshman_year=2018,
            user_type=3,
            name="기존부주장",
            major="체육교육과",
            grade=4,
            position=3
        )
        self.new_vice_captain = CustomUser.objects.create_user(
            phone_number="010-1234-9876",
            password="newvicecaptain1234",
            freshman_year=2019,
            user_type=5,
            name="새로운부주장",
            major="수학교육과",
            grade=3,
            position=6
        )
        self.url = "/api/users/handover_leadership/"
        self.data = {
            "old_captain": "010-1234-5678",
            "new_captain": "010-1234-4321",
            "old_vice_captain": "010-1234-1234",
            "new_vice_captain": "010-1234-9876",
        }

    def test_unallowed_methods(self):
        self.client.force_authenticate(user=self.old_captain)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_handover_success(self):
        self.client.force_authenticate(user=self.old_captain)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.old_captain.refresh_from_db()
        self.new_captain.refresh_from_db()
        self.old_vice_captain.refresh_from_db()
        self.new_vice_captain.refresh_from_db()

        self.assertEqual(self.old_captain.user_type, 5)
        self.assertEqual(self.new_captain.user_type, 2)
        self.assertEqual(self.old_vice_captain.user_type, 5)
        self.assertEqual(self.new_vice_captain.user_type, 3)

    def test_handover_failure(self):
        # 1. not logged in
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # 2. not captain
        self.client.force_authenticate(user=self.new_captain)
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # 3. wrong captain
        self.client.force_authenticate(user=self.old_captain)
        self.data["old_captain"] = "010-1234-4321"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 4. wrong vice captain
        self.data["old_captain"] = "010-1234-5678"
        self.data["old_vice_captain"] = "010-1234-4321"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 5. not exist
        self.data["old_captain"] = "010-1234-5678"
        self.data["old_vice_captain"] = "010-1234-1234"
        self.data["new_captain"] = "010-0000-4321"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.data["new_captain"] = "010-1234-4321"
        self.data["new_vice_captain"] = "010-0000-9876"
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class StatusChangeAPITestCase(APITestCase):
    def setUp(self):
        self.captain = CustomUser.objects.create_user(
            phone_number="010-1234-5678",
            password="captain1234",
            freshman_year=2018,
            user_type=2,
            name="주장",
            major="체육교육과",
            grade=4,
            position=3
        )
        self.manager = CustomUser.objects.create_user(
            phone_number="010-1234-4321",
            password="manager1234",
            freshman_year=2019,
            user_type=4,
            name="매니저",
            major="수학교육과",
            grade=3,
            position=6
        )
        self.player = CustomUser.objects.create_user(
            phone_number="010-1234-1234",
            password="player1234",
            freshman_year=2019,
            user_type=5,
            name="선수",
            major="수학교육과",
            grade=3,
            position=6
        )
        self.url = "/api/users/change_status/"
        self.data = {
            "new_status": "MILITARY",
            "phone_number": "010-1234-1234"
        }

    def test_unallowed_methods(self):
        self.client.force_authenticate(user=self.captain)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_status_change_success(self):
        self.client.force_authenticate(user=self.captain)
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.player.refresh_from_db()
        self.assertEqual(self.player.user_type, 6)

    def test_status_change_success_manager(self):
        self.client.force_authenticate(user=self.manager)
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.player.refresh_from_db()
        self.assertEqual(self.player.user_type, 6)

    def test_status_change_failure(self):
        # 1. not logged in
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # 2. not leadership
        self.client.force_authenticate(user=self.player)
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # 3. wrong user
        self.client.force_authenticate(user=self.captain)
        self.data["phone_number"] = "010-0000-4321"
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 4. wrong status
        self.data["phone_number"] = "010-1234-1234"
        self.data["new_status"] = "wrongstatus"
        response = self.client.patch(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
