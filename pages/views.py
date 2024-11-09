from django.shortcuts import render
from django.views.generic import TemplateView #Para mostrar un template

# Create your views here :).
class HomePageView(TemplateView): #Heredando de templateview
    template_name = "home.html" #Indicando el template a mostrar

class AboutPageView(TemplateView):
    template_name = "about.html" #Indicando el template a mostrar