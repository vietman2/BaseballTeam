# from django.shortcuts import render
# from rest_framework import viewsets
# from timetable.models import Forecast
# Create your views here.
# class WeatherViewset(viewsets.ModelViewSet):
#     serializer_class = ForecastSerializer

#     def get_queryset(self):
#         data = Forecast.objects.all()
#         return data
from rest_framework.views import APIView
from .serializers import TimetableSerializer,ForecastSerializer
from .models import Timetable
from rest_framework.response import Response
from rest_framework import status

class TimetableListView(APIView):
    def get(self,request):
        timetables = Timetable.objects.all()
        serializer = TimetableSerializer(timetables, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        date = request.data.get("date")
        total = request.data.get("total")
        drilltype = request.data.get("drilltype")
        if not date or not total or not drilltype:
            return Response({"details":"field missing"},status=status.HTTP_400_BAD_REQUEST)
        timetable = Timetable.objects.create(
            date = date,
            total = total,
            drilltype = drilltype,
        )
        serializer = TimetableSerializer(timetable)

        return Response(timetable,status= status.HTTP_201_CREATED)
