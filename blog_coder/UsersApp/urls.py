from unicodedata import name
from django.urls import path
from UsersApp import views

urlpatterns = [
    path('signup', views.register, name='Sign Up'),
    path('login', views.login_request, name= 'Login'),
    path('logout', views.CustomLogoutView.as_view(), name='Logout'),
]