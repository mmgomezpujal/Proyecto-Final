from unicodedata import name
from django.urls import path
from BlogApp import views

urlpatterns = [
    path('pages/', views.ListaArticulos.as_view(), name='Articulos'),
    path('', views.home, name='Inicio'),
    path('about/', views.about, name='Acerca de'),
    path(r'^(?P<pk>/d+)$', views.DetalleArticulos.as_view(), name="Detail"),
]