from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from pet.models import AdoptionPets, Pet


class AdoptionContactPage(LoginRequiredMixin, TemplateView):
    template_name = "conta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet_id = self.kwargs.get("pet_id")
        pet = get_object_or_404(Pet, id=pet_id)
        owner = pet.owner

        context["pet"] = pet
        context["owner"] = owner
        return context


class AdoptPetView(LoginRequiredMixin, View):
    def post(self, request, pk):
        pet = get_object_or_404(Pet, pk=pk)
        adoption_pets, created = AdoptionPets.objects.get_or_create(
            user=request.user, pet=pet
        )
        adoption_pets.adoption = True
        adoption_pets.save()
        return redirect("adoption:adoption-contact", pet_id=pk)


class AdoptionPetsList(LoginRequiredMixin, ListView):
    model = Pet
    template_name = "adoptionPets.html"
    context_object_name = "pet"

    def get_queryset(self):
        adoption_pets = AdoptionPets.objects.filter(
            user=self.request.user, adoption=True
        ).values_list("pet", flat=True)
        return Pet.objects.filter(id__in=adoption_pets)
