from django.shortcuts import render
from django.views.generic import TemplateView , ListView
from .models import Prueba

# Create your views here.
class IndexView(TemplateView):
    template_name='home.html'

class PruebaListView(ListView):
    template_name='lista.html'
    queryset=['Python','Django','AWS',]
    context_object_name='lista_prueba'

class ModeloPruebaListView(ListView):
    model= Prueba
    template_name='prueba.html'
    context_object_name='prueba'



