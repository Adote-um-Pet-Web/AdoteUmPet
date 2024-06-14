from django.urls import path

app_name = "userauths"

from .views import (
    LoginView,
    LogoutView,
    PageConfigUser,
    SignUpView,
    UserProfileDeleteView,
    UserProfileUpdateView,
)

urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("sign-in/", LoginView.as_view(), name="sign-in"),
    path("logout/", LogoutView.as_view(), name="sign-out"),
    path("delete/<uuid:pk>/", UserProfileDeleteView.as_view(), name="user-delete"),
    path("update/<uuid:pk>/", UserProfileUpdateView.as_view(), name="user-update"),
    path("config/", PageConfigUser.as_view(), name="user-config"),
]
