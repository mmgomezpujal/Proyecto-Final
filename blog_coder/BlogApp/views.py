from nntplib import ArticleInfo
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
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


class DetalleArticulos(DetailView):
    model = Articulo
    template_name = "BlogApp/page_id.html"

# Create your views here.
