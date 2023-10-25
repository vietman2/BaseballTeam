from rest_framework import serializers

from .models import Session, TrainingType, Attendance

class SessionSerializer(serializers.ModelSerializer):
    day = serializers.CharField(source='get_day_display')

    class Meta:
        model = Session
        fields = '__all__'

class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
