from django.contrib import admin
from django.urls import path
from . import views

app_name = "pets"

urlpatterns = [
    path("", views.PageView.as_view(), name="index"),

]
