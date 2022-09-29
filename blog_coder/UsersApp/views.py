from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from UsersApp.forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from UsersApp.forms import UserEditForm


def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario,password=contra)

            if user is not None: 
                login(request, user)

                return render(request, "BlogApp/home.html", {"mensaje":f"Bienvenido {usuario}"})
            else:

                return render(request, "BlogApp/home.html", {"mensaje": "Error, datos incorrectos"})

        else:

            return render(request, "BlogApp/home.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "UsersApp/login.html", {'form': form})


def register(request):
    
    if request.method == 'POST':

        form_1 = UserRegisterForm(request.POST)

        if form_1.is_valid():

            username = form_1.cleaned_data['username']
            form_1.save()
            return render(request, "BlogApp/home.html", {"mensaje":"Usuario Creado"})
    
    else: 
        form_1=UserRegisterForm()

    return render(request, "UsersApp/registro.html", {"form_1":form_1})


class CustomLogoutView(LogoutView):
    template_name = 'UsersApp/logout.html'


@login_required
def EditarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "BlogApp/home.html", {"mensaje": "La información se ha modificado con éxito"})
    
    else: 
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "UsersApp/editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

# Create your views here.
