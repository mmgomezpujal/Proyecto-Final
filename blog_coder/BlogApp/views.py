from django.shortcuts import render

def home(request):
    return render (request, 'BlogApp/home.html')


def about(request):
    return render (request, 'BlogApp/about.html')


def pages(request):
    return render (request, 'BlogApp/pages.html')
# Create your views here.
