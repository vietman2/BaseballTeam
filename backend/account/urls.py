from django.urls import path
from .views import SigninView, SignupStep1View, SignupStep2View, LogoutView

app_name = 'account'
urlpatterns = [
    path("signup/step1/", SignupStep1View.as_view()),
    path("signup/step2/", SignupStep2View.as_view()),   
    path("signin/", SigninView.as_view()),
    path("logout/", LogoutView.as_view()),
]