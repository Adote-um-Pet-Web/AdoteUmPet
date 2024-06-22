from django.urls import path, register_converter

from . import views

app_name = "pets"

from uuid import UUID


class UUIDConverter:
    regex = (
        "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    )

    def to_python(self, value):
        return UUID(value)

    def to_url(self, value):
        return str(value)


register_converter(UUIDConverter, "uuid")

urlpatterns = [
    path("", views.PagePetIndex.as_view(), name="index"),
    path("pet-faq/", views.PageFaqQuestions.as_view(), name="pet-faq"),
    path("pet-dashboard/", views.PageDashBoard.as_view(), name="pet-dashboard"),
    path("pet-saves/", views.PagePetSaves.as_view(), name="pet-saves"),
    path("pet-added/", views.PagePetAdded.as_view(), name="pet-added"),
    path("pet-delete/<uuid:pk>/", views.DeletePetView.as_view(), name="pet-delete"),
    path("pet/update/<uuid:pk>/", views.UpdatePetView.as_view(), name="update_pet"),
    path(
        "pet/toggle_adopted/<uuid:pk>/",
        views.ToggleAdoptedView.as_view(),
        name="toggle_adopted",
    ),
    path(
        "pet/update/history/<uuid:pet_id>/",
        views.UpdateHistoryPetView.as_view(),
        name="update_history_pet",
    ),
    path(
        "pet/update/medical_record/<uuid:pet_id>/",
        views.UpdateMedicalRecordView.as_view(),
        name="update_medical_record",
    ),
    path(
        "pet/update/images/<uuid:pet_id>/",
        views.UpdateImagesPetsView.as_view(),
        name="update_images_pets",
    ),
    path("pet/<uuid:pk>/", views.PageDetailPet.as_view(), name="pet_detail"),
    path(
        "pet/<uuid:pk>/favorited/",
        views.ToggleFavoritedView.as_view(),
        name="toggle_favorited",
    ),
    path(
        "pet/<uuid:pk>/favorited-save/",
        views.ToggleFavoritedSavedView.as_view(),
        name="toggle_favorited_saved",
    ),
    path("create_pet/", views.CreatePetView.as_view(), name="create_pet"),
    path(
        "create_history_pet/<uuid:pet_id>/",
        views.CreateHistoryPetView.as_view(),
        name="create_history_pet",
    ),
    path(
        "create_medical_record/<uuid:pet_id>/",
        views.CreateMedicalRecordView.as_view(),
        name="create_medical_record",
    ),
    path(
        "create_images_pets/<uuid:pet_id>/",
        views.CreateImagesPetsView.as_view(),
        name="create_images_pets",
    ),
]
