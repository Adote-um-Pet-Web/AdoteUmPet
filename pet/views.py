from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
from django.views.generic.list import ListView

from userauth.models import User

from . import models
from .forms import HistoryPetForm, ImagesPetsForm, MedicalRecordForm, PetForm
from .models import BannerImagens, Pet


class PagePetIndex(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"

    def get_queryset(self):
        return models.Pet.objects.filter(adopted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banner_images"] = BannerImagens.objects.all()
        return context


class PageFaqQuestions(ListView):
    model = models.Pet
    context_object_name = "pet"
    template_name = "faqQuestions.html"


class PageDashBoard(ListView):
    model = models.Pet
    context_object_name = "pet"
    template_name = "dashboard/dashboard.html"

    @method_decorator(login_required)
    @method_decorator(user_passes_test(lambda user: user.is_staff))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PageDetailPet(DetailView):
    model = models.Pet
    context_object_name = "pet"
    template_name = "petDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        user = self.request.user
        if user.is_authenticated:
            favorited_pet = models.FavoritedPet.objects.filter(
                user=user, pet=pet
            ).first()
            context["is_favorited"] = (
                favorited_pet.favorited if favorited_pet else False
            )
        else:
            context["is_favorited"] = False
        return context


class PagePetSaves(LoginRequiredMixin, ListView):
    model = Pet
    template_name = "petSave.html"
    context_object_name = "pet"

    def get_queryset(self):
        favorited_pets = models.FavoritedPet.objects.filter(
            user=self.request.user, favorited=True
        ).values_list("pet", flat=True)
        return Pet.objects.filter(id__in=favorited_pets)


class PagePetAdded(LoginRequiredMixin, ListView):
    model = models.Pet
    template_name = "petAdded.html"
    context_object_name = "pet"

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)


class ToggleAdoptedView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pet = get_object_or_404(Pet, id=self.kwargs["pk"])
        pet.adopted = not pet.adopted
        pet.save()
        return redirect("pets:pet-added")


class ToggleFavoritedView(LoginRequiredMixin, View):
    def post(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        favorited_pet, created = models.FavoritedPet.objects.get_or_create(
            user=request.user, pet=pet
        )
        favorited_pet.favorited = not favorited_pet.favorited
        favorited_pet.save()
        return redirect("pets:pet_detail", pk=pk)


class ToggleFavoritedSavedView(LoginRequiredMixin, View):
    def post(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        favorited_pet, created = models.FavoritedPet.objects.get_or_create(
            user=request.user, pet=pet
        )
        favorited_pet.favorited = not favorited_pet.favorited
        favorited_pet.save()
        return redirect("pets:pet-saves")


class DeletePetView(LoginRequiredMixin, DeleteView):
    model = models.Pet
    context_object_name = "pet"
    template_name = "petDeleteConfirm.html"
    success_url = reverse_lazy("pets:index")

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


# CREATE PET
class CreatePetView(LoginRequiredMixin, CreateView):
    form_class = PetForm
    template_name = "createPet.html"
    context_object_name = "pet"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return redirect("pets:create_history_pet", pet_id=self.object.id)


class CreateHistoryPetView(LoginRequiredMixin, CreateView):
    form_class = HistoryPetForm
    template_name = "createHistory.html"
    context_object_name = "pet"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]

        return context

    def get_success_url(self):
        return reverse_lazy(
            "pets:create_medical_record", kwargs={"pet_id": self.kwargs["pet_id"]}
        )

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs["pet_id"])
        return super().form_valid(form)


class CreateMedicalRecordView(LoginRequiredMixin, CreateView):
    form_class = MedicalRecordForm
    template_name = "createMedicalRecord.html"
    context_object_name = "pet"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]
        return context

    def get_success_url(self):
        return reverse_lazy(
            "pets:create_images_pets", kwargs={"pet_id": self.kwargs["pet_id"]}
        )

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs["pet_id"])
        return super().form_valid(form)


class CreateImagesPetsView(LoginRequiredMixin, CreateView):
    form_class = ImagesPetsForm
    template_name = "createImagePets.html"
    context_object_name = "pet"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]

        return context

    def get_success_url(self):
        return reverse_lazy("pets:index")

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs["pet_id"])
        return super().form_valid(form)


# UPDATE PET
class UpdatePetView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "petUpdate/petUpdate.html"
    context_object_name = "pet"

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        return redirect("pets:update_history_pet", pet_id=self.object.id)


class UpdateHistoryPetView(LoginRequiredMixin, UpdateView):
    form_class = HistoryPetForm
    template_name = "petUpdate/petUpdateHistory.html"
    context_object_name = "history"

    def get_object(self):
        return models.HistoryPet.objects.get(id_pet=self.kwargs["pet_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]
        return context

    def get_success_url(self):
        return reverse_lazy(
            "pets:update_medical_record", kwargs={"pet_id": self.kwargs["pet_id"]}
        )


class UpdateMedicalRecordView(LoginRequiredMixin, UpdateView):
    form_class = MedicalRecordForm
    template_name = "petUpdate/petUpdateMedicalRecord.html"
    context_object_name = "medical_record"

    def get_object(self):
        return models.MedicalRecord.objects.get(id_pet=self.kwargs["pet_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]
        return context

    def get_success_url(self):
        return reverse_lazy(
            "pets:update_images_pets", kwargs={"pet_id": self.kwargs["pet_id"]}
        )


class UpdateImagesPetsView(LoginRequiredMixin, UpdateView):
    form_class = ImagesPetsForm
    template_name = "petUpdate/petUpdateImagens.html"
    context_object_name = "images"

    def get_object(self):
        return models.ImagesPets.objects.get(id_pet=self.kwargs["pet_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_id"] = self.kwargs["pet_id"]
        return context

    def get_success_url(self):
        return reverse_lazy("pets:index")
