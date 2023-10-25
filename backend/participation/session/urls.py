from django.urls import path

from .views import TrainingTypeAPI

urlpatterns = [
    #path('<int:pk>', SessionAPI.as_view()),
    path('trainingtypes/', TrainingTypeAPI.as_view()),
]
