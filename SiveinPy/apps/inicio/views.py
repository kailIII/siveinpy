from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

# Create your views here.

class index(TemplateView):
	template_name = 'inicio/index.html'


class index2(TemplateView):
	template_name = "inicio/index2.html"