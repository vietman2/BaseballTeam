from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Session, TrainingType, Attendance
from .serializers import SessionSerializer, TrainingTypeSerializer, AttendanceSerializer
from user.permissions import IsLeadership

class TrainingTypeAPI(GenericAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    #permission_classes = [IsAuthenticated, IsLeadership]

    @extend_schema(summary="훈련 유형 리스트 조회", tags=["훈련 유형 관리"])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TrainingTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary="훈련 유형 생성", tags=["훈련 유형 관리"])
    def post(self, request, *args, **kwargs):
        serializer = TrainingTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class SessionView(RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    @extend_schema(summary="훈련 세션 조회", tags=["훈련 세션 관리"])
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SessionSerializer(instance)
        return Response(serializer.data)

class AttendanceView(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
