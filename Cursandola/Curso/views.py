from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    temas = Tema_General.objects.all()
    context = { 'temas':temas}
    return render(request, 'Curso/index.html', context)

def login(request):
    return render(request, 'Curso/login.html')

def register(request):
    return render(request, 'Curso/register.html')

def categoria(request):
    categorias = Categoria.objects.all()
    context = {'categorias':categorias}
    return render(request, 'Curso/categoria.html', context)

