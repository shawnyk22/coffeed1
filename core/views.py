from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.def TestView{}

class SplashView(TemplateView):
	template_name = "index.html"