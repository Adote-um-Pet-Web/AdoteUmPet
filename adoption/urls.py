from django.urls import path

from . import views

app_name = "adoption"

urlpatterns = [
    path(
        "contact/<uuid:pet_id>/",
        views.AdoptionContactPage.as_view(),
        name="adoption-contact",
    ),
    path("adoption-pet/<uuid:pk>/", views.AdoptPetView.as_view(), name="adoption-pet"),
    path(
        "share-pet-adoption/<uuid:pet_id>/",
        views.SharePetAdoption.as_view(),
        name="share-pet-adoption",
    ),
    path("share-pet/<uuid:pk>/", views.SharedPet.as_view(), name="share-pet"),
    path("adoption-list/", views.AdoptionPetsList.as_view(), name="adoption-list"),
    path("check-fields/", views.CheckFieldsView.as_view(), name="check-fields"),
]
