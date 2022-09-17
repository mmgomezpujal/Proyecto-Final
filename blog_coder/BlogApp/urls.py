from unicodedata import name
from django.urls import path
from BlogApp import views

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('acerca-de/', views.about, name='Acerca de'),
    path('articulos/', views.pages, name='Articulos'),
]