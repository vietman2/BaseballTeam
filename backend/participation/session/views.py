from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView

from .models import Session, TrainingType, Attendance
from .serializers import SessionSerializer, TrainingTypeSerializer, AttendanceSerializer

class TrainingTypeAPI(ListCreateAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer

class SessionView(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class AttendanceView(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
