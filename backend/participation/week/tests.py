import datetime
from rest_framework.test import APITestCase
from rest_framework import status

from user.models import CustomUser
from participation.week.models import Week

class WeekAPITestCase(APITestCase):
    def setUp(self):
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
        self.normal_user = CustomUser.objects.create_user(
            phone_number="010-1234-1234",
            password="normaluser1234",
            freshman_year=2019,
            user_type=5,
            name="일반유저",
            major="수학교육과",
            grade=3,
            position=6
        )
        self.monday_date = Week.objects.get_next_monday_date()
        self.data = {
            "yr_mn_wk": Week.objects.format_next_monday(self.monday_date),
            "year": self.monday_date.year,
            "month": self.monday_date.month,
            "week": (self.monday_date.day - 1) // 7 + 1,
            "start_date": self.monday_date,
            "end_date": self.monday_date + datetime.timedelta(days=6),
            "monday": {
                "date": self.monday_date,
                "training_type": {
                    "id": 1,
                    "type": "일반",
                    "description": "일반 훈련"
                },
                "start_time": {
                    "hour": 17,
                    "minute": 0
                },
                "end_time": {
                    "hour": 21,
                    "minute": 0
                }
            },
            "tuesday": {
                "date": self.monday_date + datetime.timedelta(days=1),
                "training_type": {
                    "id": 2,
                    "type": "일반-필참-오후",
                    "description": "필수 참여 오후 훈련 (주로 화요일)"
                },
                "start_time": {
                    "hour": 17,
                    "minute": 0
                },
                "end_time": {
                    "hour": 21,
                    "minute": 0
                }
            },
            "wednesday": {
                "date": self.monday_date + datetime.timedelta(days=2),
                "training_type": {
                    "id": 1,
                    "type": "일반",
                    "description": "일반 훈련"
                },
                "start_time": {
                    "hour": 17,
                    "minute": 0
                },
                "end_time": {
                    "hour": 21,
                    "minute": 0
                }
            },
            "thursday": {
                "date": self.monday_date + datetime.timedelta(days=3),
                "training_type": {
                    "id": 1,
                    "type": "일반",
                    "description": "일반 훈련"
                },
                "start_time": {
                    "hour": 17,
                    "minute": 0
                },
                "end_time": {
                    "hour": 21,
                    "minute": 0
                }
            },
            "friday": {
                "date": self.monday_date + datetime.timedelta(days=4),
                "training_type": {
                    "id": 1,
                    "type": "일반",
                    "description": "일반 훈련"
                },
                "start_time": {
                    "hour": 17,
                    "minute": 0
                },
                "end_time": {
                    "hour": 21,
                    "minute": 0
                }
            },
            "saturday": {
                "date": self.monday_date + datetime.timedelta(days=5),
                "training_type": {
                    "id": 3,
                    "type": "일반-필참-오전",
                    "description": "필수 참여 오전 훈련 (주로 토요일)"
                },
                "start_time": {
                    "hour": 8,
                    "minute": 30
                },
                "end_time": {
                    "hour": 13,
                    "minute": 0
                }
            },
            "sunday": {
                "date": self.monday_date + datetime.timedelta(days=6),
                "training_type": {
                    "id": 6,
                    "type": "훈련없음",
                    "description": "훈련 없음"
                },
            }
        }

    def test_form(self):
        self.client.force_authenticate(self.manager)
        response = self.client.get("/api/weeks/form/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_form_fail(self):
        # not authenticated
        response = self.client.get("/api/weeks/form/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # not leader
        self.client.force_authenticate(self.normal_user)
        response = self.client.get("/api/weeks/form/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # already created
        self.client.force_authenticate(self.manager)
        self.client.post("/api/weeks/", self.data, format="json")
        # set server time to oct 28th, 2023
        response = self.client.get("/api/weeks/form/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create(self):
        self.client.force_authenticate(self.manager)
        response = self.client.post("/api/weeks/", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_fail(self):
        # not authenticated
        response = self.client.post("/api/weeks/", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # not leader
        self.client.force_authenticate(self.normal_user)
        response = self.client.post("/api/weeks/", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # already created
        self.client.force_authenticate(self.manager)
        self.client.post("/api/weeks/", self.data, format="json")
        response = self.client.post("/api/weeks/", self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list(self):
        self.client.force_authenticate(self.manager)
        response = self.client.get("/api/weeks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.post("/api/weeks/", self.data, format="json")
        response = self.client.get("/api/weeks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # non leaders can also see the list
        self.client.force_authenticate(self.normal_user)
        response = self.client.get("/api/weeks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_fail(self):
        # not authenticated
        response = self.client.get("/api/weeks/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
