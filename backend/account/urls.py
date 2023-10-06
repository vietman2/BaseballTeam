from django.urls import path, include

from .views import RegisterView, UserProfileView, ChangePasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("user/", UserProfileView.as_view(), name="user"),
]
