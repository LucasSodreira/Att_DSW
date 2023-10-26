from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def livros_por_autor(request, autor_nome):
    livros = Livro.objects.filter(autor=autor_nome)
    return render(request, 'livros_por_autor.html', {'livros': livros})
