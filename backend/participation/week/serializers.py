import datetime
from rest_framework import serializers

from .models import Week
from participation.session.models import TrainingType
from participation.session.serializers import TrainingTypeSerializer

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = "__all__"

class WeeklyFormSerializer(serializers.Serializer):
    training_types = serializers.SerializerMethodField()
    yr_mn_wk = serializers.CharField()
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    week = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def get_training_types(self, obj):
        training_types = TrainingType.objects.all()
        return TrainingTypeSerializer(training_types, many=True).data

class WeekListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ["id", "yr_mn_wk", "year", "month", "week", "start_date", "end_date"]
