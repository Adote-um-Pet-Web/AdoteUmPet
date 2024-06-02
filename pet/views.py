from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, View
from django.views.generic.list import ListView

from . import models
from .forms import HistoryPetForm, ImagesPetsForm, MedicalRecordForm, PetForm
from .models import Pet


class PagePetIndex(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"


class ToggleFavoritedView(View):
    def post(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        pet.favorited = not pet.favorited
        pet.save()
        return redirect("pets:pet_detail", pk=pk)


class PageDetailPet(DetailView):
    model = models.Pet
    context_object_name = "pet"
    template_name = "petDetail.html"


class PagePetSaves(ListView):
    model = models.Pet
    template_name = "petSave.html"
    context_object_name = "pet"


class PagePetAdded(ListView):
    model = models.Pet
    template_name = "petAdded.html"
    context_object_name = "pet"


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
