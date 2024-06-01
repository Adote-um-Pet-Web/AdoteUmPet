from django.urls import path

from . import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-in/", views.login_view, name="sign-in"),
    path("sign-out/", views.logout_view, name="sign-out"),
    path('user-update/<uuid:pk>/', views.PageUpdateUser.as_view(), name='user-update'),
    path('user-config/', views.PageConfigUser.as_view(), name='user-config')
    ]
