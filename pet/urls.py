from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.PageView.as_view(), name="index"),

]
