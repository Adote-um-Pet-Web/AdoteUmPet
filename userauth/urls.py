from django.urls import path

from . import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-in/", views.login_view, name="sign-in"),
    path("sign-out/", views.logout_view, name="sign-out"),
    path(
        "user-update/<uuid:pk>/",
        views.UserProfileUpdateView.as_view(),
        name="user-update",
    ),
    path("user-config/", views.PageConfigUser.as_view(), name="user-config"),
    path("contact-page/", views.ContactPage.as_view(), name="contact-page"),
    path("insta-test/", views.InstaTest.as_view(), name="insta-test/"),
]
