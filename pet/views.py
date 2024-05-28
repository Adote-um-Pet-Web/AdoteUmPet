
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import  reverse_lazy
from . import models
from django.views.generic import CreateView
from .forms import PetForm, HistoryPetForm, MedicalRecordForm, ImagesPetsForm
from .models import Pet
from django.shortcuts import redirect


class PagePetIndex(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"


class PageNavForm(LoginRequiredMixin, ListView):
    model = models.Pet
    template_name = 'navForm.html'
    context_object_name = "pet"



class CreatePetView(CreateView):
    form_class = PetForm
    template_name = 'createPet.html'
    context_object_name = "pet"

    def form_valid(self, form):
        form.instance.owner = self.request.user

        self.object = form.save()

        return redirect('pets:create_history_pet', pet_id=self.object.id)

class CreateHistoryPetView(CreateView):
    form_class = HistoryPetForm
    template_name = 'createHistory.html'

    def get_success_url(self):
        return reverse_lazy('pets:create_medical_record', kwargs={'pet_id': self.kwargs['pet_id']})

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs['pet_id'])
        return super().form_valid(form)


class CreateMedicalRecordView(CreateView):
    form_class = MedicalRecordForm
    template_name = 'createMedicalRecord.html'

    def get_success_url(self):
        return reverse_lazy('pets:create_images_pets', kwargs={'pet_id': self.kwargs['pet_id']})

    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs['pet_id'])
        return super().form_valid(form)

class CreateImagesPetsView(CreateView):
    form_class = ImagesPetsForm
    template_name = 'createImagePets.html'


    def get_success_url(self):
        return reverse_lazy('pets:index')


    def form_valid(self, form):
        form.instance.id_pet = Pet.objects.get(id=self.kwargs['pet_id'])
        return super().form_valid(form)

class PageDetailPet(LoginRequiredMixin, DetailView):
    model = models.Pet
    context_object_name = 'pet'
    template_name = 'petDetail.html'
