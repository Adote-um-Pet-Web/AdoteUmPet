from django.urls import path
from . import views
from django.urls import register_converter

app_name = "pets"

from uuid import UUID

class UUIDConverter:
    regex = "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    def to_python(self, value):
        return UUID(value)
    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path("", views.PagePetIndex.as_view(), name="index"),
    path("navform/", views.PageNavForm.as_view(), name="navform"),

    path("create_pet/", views.CreatePetView.as_view(), name="create_pet"),
    path('create_history_pet/<uuid:pet_id>/', views.CreateHistoryPetView.as_view(), name='create_history_pet'),
    path('create_medical_record/<uuid:pet_id>/', views.CreateMedicalRecordView.as_view(), name='create_medical_record'),
    path('create_images_pets/<uuid:pet_id>/', views.CreateImagesPetsView.as_view(), name='create_images_pets'),
    path('pet/<int:pk>/', views.PageDetailPet.as_view(), name='pet-detail'),

]

