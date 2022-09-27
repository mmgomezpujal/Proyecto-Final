from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


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

        form_1 = UserCreationForm(request.POST)

        if form_1.is_valid():

            username = form_1.cleaned_data['username']
            form_1.save()
            return render(request, "BlogApp/home.html", {"mensaje":"Usuario Creado"})
    
    else: 
        form_1=UserCreationForm()

    return render(request, "UsersApp/registro.html", {"form_1":form_1})

# Create your views here.
