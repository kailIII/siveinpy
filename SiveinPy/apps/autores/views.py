from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import Autor
from django.core.urlresolvers import reverse_lazy

class RegistrarAutor(CreateView):
	template_name = 'autores/registrar.html'
	model = Autor
	success_url = reverse_lazy('mostrar_autor')

class MostrarAutor(TemplateView): 
	template_name = 'autores/mostrar.html'
	