from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Disco

# Create your views here.

def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'lista_discos.html', {'discos': discos})

def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Disco, id=disco_id)
    return render(request, 'detalhes_disco.html', {'disco': disco})