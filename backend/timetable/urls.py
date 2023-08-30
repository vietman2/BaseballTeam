from django.urls import path
from django.conf.urls import include,url
from .views import WeatherViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data',WeatherViewset, basename='weather-data')  #data라는 경로로 들어오는 요청을 weatherviewset과 연결시킴

urlpatterns = [
    url('',include(router.urls)),
]
