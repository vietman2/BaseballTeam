from django.urls import path

from .views import RegisterView, UserProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # path()
    path("user/", UserProfileView.as_view(), name="user"),
]
