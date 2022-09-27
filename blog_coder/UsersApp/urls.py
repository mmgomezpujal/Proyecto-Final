from unicodedata import name
from django.urls import path
from UsersApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sign-up', views.register, name='Sign Up'),
    path('login', views.login_request, name= 'Login'),
    path('logout', LogoutView.as_view(template_name = "UsersApp/logout.html"), name='Logout')
]