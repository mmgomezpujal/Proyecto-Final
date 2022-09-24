from unicodedata import name
from django.urls import path
from BlogApp import views
from BlogApp.models import Articulo

urlpatterns = [
    path('pages/', views.ListaArticulos.as_view(), name='Articulos'),
    path('', views.home, name='Inicio'),
    path('about/', views.about, name='Acerca de'),
    path(r'^(?P<pk>/d+)$', views.DetalleArticulos.as_view(), name="Detalle"),
    path(r'^nuevo$', views.CrearArticulo.as_view(model = Articulo, success_url = '/blog-viajes/pages'), name='Nuevo'),
    path(r'^editar/(?P<pk>/d+)$', views.EditarArticulo.as_view(model = Articulo, success_url = '/blog-viajes/pages'), name='Editar'),
    path(r'^borrar/(?P<pk>/d+)$', views.EliminarArticulo.as_view(model = Articulo, success_url = '/blog-viajes/pages'), name='Eliminar'),
]