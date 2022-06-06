from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 

from classroom.models import Teacher
from django.urls import reverse,reverse_lazy

# Create your views here.
class HomeView(TemplateView):
  template_name = 'classroom/home.html'

