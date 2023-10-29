import datetime
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Week
from .serializers import WeekSerializer, WeeklyFormSerializer, WeekListSerializer
from user.permissions import IsLeadership

class WeekViewSet(ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    @extend_schema(summary="훈참표 생성", tags=["훈참표 관리"])
    def create(self, request, *args, **kwargs):
        if not IsLeadership().has_permission(request, self):
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

        monday = Week.objects.create_session("monday", request.data)
        tuesday = Week.objects.create_session("tuesday", request.data)
        wednesday = Week.objects.create_session("wednesday", request.data)
        thursday = Week.objects.create_session("thursday", request.data)
        friday = Week.objects.create_session("friday", request.data)
        saturday = Week.objects.create_session("saturday", request.data)
        sunday = Week.objects.create_session("sunday", request.data)

        week_data = {
            "yr_mn_wk": request.data["yr_mn_wk"],
            "year": request.data["year"],
            "month": request.data["month"],
            "week": request.data["week"],
            "start_date": request.data["start_date"],
            "end_date": request.data["end_date"],
            "monday": monday.id,
            "tuesday": tuesday.id,
            "wednesday": wednesday.id,
            "thursday": thursday.id,
            "friday": friday.id,
            "saturday": saturday.id,
            "sunday": sunday.id
        }

        serializer = WeekSerializer(data=week_data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(summary="훈참표 폼 받기", tags=["훈참표 관리"])
    @action(
        detail=False,
        methods=['get'],
        serializer_class=WeeklyFormSerializer,
        permission_classes=[IsAuthenticated, IsLeadership]
    )
    def form(self, request, *args, **kwargs):
        # get next monday's yr_mn_wk
        next_monday = datetime.date.today() + datetime.timedelta(days=-datetime.datetime.today().weekday(), weeks=1)
        next_monday_yr_mn_wk = f"{next_monday.year}년 {next_monday.month}월 {(next_monday.day - 1) // 7 + 1}주차"

        if Week.objects.is_week_created(next_monday_yr_mn_wk):
            return Response({"detail": "이미 훈참표가 생성되었습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # get start_date and end_date of next week
        start_date = next_monday
        end_date = start_date + datetime.timedelta(days=6)
        yr_mn_wk = next_monday_yr_mn_wk
        year = next_monday.year
        month = next_monday.month
        week = (next_monday.day - 1) // 7 + 1

        week_data = {
            "yr_mn_wk": yr_mn_wk,
            "year": year,
            "month": month,
            "week": week,
            "start_date": start_date,
            "end_date": end_date
        }

        serializer = WeeklyFormSerializer(data=week_data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary="과거 훈참표 전부 조회", tags=["훈참표 관리"])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = WeekListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(summary="훈참표 1개 조회", tags=["훈참표 관리"])
    def retrieve(self, request, *args, **kwargs):
        """
            TODO: 이거 구현하기
        """
        return super().retrieve(request, *args, **kwargs)

