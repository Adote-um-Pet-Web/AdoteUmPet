from django.contrib import admin
from django.urls import path

from . import views

app_name = "pets"

urlpatterns = [
    path("", views.PagePetIndex.as_view(), name="index"),
    path("newpet/", views.PageNewPet.as_view(), name="newpet"),
    path('pet/<int:pk>/', views.PageDetailPet.as_view(), name='pet-detail'),
]
