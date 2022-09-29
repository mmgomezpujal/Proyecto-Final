from nntplib import ArticleInfo
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class CrearArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    success_url = reverse_lazy('Articulos')
    fields = ['titulo', 'subtitulo', 'fecha', 'autor', 'email_autor', 'cuerpo', 'imagen']


class EditarArticulo(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = reverse_lazy('Articulos')
    fields = ['titulo', 'subtitulo', 'fecha', 'autor', 'email_autor', 'cuerpo']


class EliminarArticulo(LoginRequiredMixin, DeleteView): 
    model = Articulo
    success_url = reverse_lazy('Articulos')

# Create your views here.
