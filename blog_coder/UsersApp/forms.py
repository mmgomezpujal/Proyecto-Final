from re import M
from socket import fromshare
from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=128)
    email = forms.EmailField()
    nombre = forms.CharField(max_length=128)
    apellido = forms.CharField(max_length=128)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

    