
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from . import models

from django.views.generic import CreateView
from .forms import PetForm, HistoryPetForm, MedicalRecordForm, ImagesPetsForm
from .models import Pet, ImagesPets, Image  # Importe o modelo Image

from django.shortcuts import render, redirect

from .models import Pet, ImagesPets

from .forms import ImagesPetsForm


class PagePetIndex(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"


class PageNewPet(LoginRequiredMixin, CreateView):
    model = models.Pet
    fields = ['name', 'species', 'breed', 'age', 'color',  'sex', 'size', 'weight','adopted']
    success_url = reverse_lazy('pets:index')
    template_name = 'registerPet.html'



    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class CreatePetView(CreateView):
    form_class = PetForm
    template_name = 'registerPet.html'
    success_url = reverse_lazy('pets:index')
    context_object_name = "pet"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CreateHistoryPetView(CreateView):
    form_class = HistoryPetForm
    template_name = 'createHistory.html'

    def get_success_url(self):
        return reverse_lazy('pets:index')

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs['pet_id'])
        return super().form_valid(form)

class CreateMedicalRecordView(CreateView):
    form_class = MedicalRecordForm
    template_name = 'createMedicalRecord.html'

    def get_success_url(self):
        return reverse_lazy('pets:index')

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs['pet_id'])
        return super().form_valid(form)


class ImagesPetsCreateView(CreateView):
    model = ImagesPets
    form_class = ImagesPetsForm
    template_name = 'sua_template.html'  # Substitua 'sua_template.html' pelo nome do seu template

    def form_valid(self, form):
        # Adicione lógica adicional aqui, se necessário
        return super().form_valid(form)

class PageDetailPet(LoginRequiredMixin, DetailView):
    model = models.Pet
    context_object_name = 'pet'
    template_name = 'petDetail.html'
