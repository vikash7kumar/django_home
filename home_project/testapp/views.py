from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name="testapp/home.html"
class About(TemplateView):
    template_name="testapp/about.html"
