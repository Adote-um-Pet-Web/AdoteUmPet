from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from . import models


class PagePetIndex(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"


class PageNewPet(LoginRequiredMixin, CreateView):
    model = models.Pet
    fields = ['name', 'species', 'breed', 'age', 'color',  'sex', 'size', 'weight','history','observations','image_profile','adopted']
    success_url = reverse_lazy('pets:index')
    template_name = 'registerPet.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PageDetailPet(LoginRequiredMixin, DetailView):
    model = models.Pet
    context_object_name = 'pet'
    template_name = 'petDetail.html'
