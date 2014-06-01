from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

# Create your views here.

def index(request):
	return render_to_response('inicio/index.html')


class index2(TemplateView):
	template_name = "inicio/index2.html"