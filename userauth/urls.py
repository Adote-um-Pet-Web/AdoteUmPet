from django.urls import path

from . import views

app_name = "userauths"

from .views import (
    ContactPage,
    InstaTest,
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
    path("user/delete/<uuid:pk>/", UserProfileDeleteView.as_view(), name="user-delete"),
    path("user/update/<uuid:pk>/", UserProfileUpdateView.as_view(), name="user-update"),
    path("user/config/", PageConfigUser.as_view(), name="user-config"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("insta-test/", InstaTest.as_view(), name="insta-test"),
]
