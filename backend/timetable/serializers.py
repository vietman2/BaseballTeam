from rest_framework import serializers
from .models import Forecast,Timetable
from tag.serializers import TagSerializer


class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ["temperature","description"]

class TimetableSerializer(serializers.ModelSerializer):
    forecast = ForecastSerializer
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Timetable
        fields = "__all__"