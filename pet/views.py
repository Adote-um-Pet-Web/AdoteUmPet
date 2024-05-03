from django.shortcuts import render
from django.views.generic.list import ListView
from . import models


class PageView(ListView):
    model = models.Pet
    template_name = "index.html"
    context_object_name = "pet"
