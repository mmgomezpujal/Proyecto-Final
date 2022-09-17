from django.shortcuts import render
from django.views.generic import ListView
from BlogApp.models import*

def home(request):
    return render (request, 'BlogApp/home.html')


def about(request):
    return render (request, 'BlogApp/about.html')


def pages(request):
    return render (request, 'BlogApp/pages.html')


class ListaArticulos(ListView):
    model = Articulo
    template_name = 'BlogApp/pages.html'

# Create your views here.
