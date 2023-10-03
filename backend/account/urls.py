from django.urls import path

from .views import SignupView, SigninView, LogoutView, PasswordChangeView, AuthorityCheckView, UserProfileView

app_name = 'account'
urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("signin/", SigninView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("change_password/", PasswordChangeView.as_view()),
    path("check/", AuthorityCheckView.as_view()),
    # path("profile/", UserProfileView.as_view()),
]
