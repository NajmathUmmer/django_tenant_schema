from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from .models import Tenant,Task

# Create your views here.
class Home(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'home.html'
class List(ListView):
    model = Task
    template_name = 'base.html'
    



