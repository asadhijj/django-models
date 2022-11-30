from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snack

class HomePage(TemplateView):
    template_name='home.html'

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack