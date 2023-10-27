from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Disco

from django.shortcuts import render, redirect
from .forms import DiscoForm
# Create your views here.


def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'lista_discos.html', {'discos': discos})


def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Disco, id=disco_id)
    return render(request, 'detalhes_disco.html', {'disco': disco})


def listar_discos(request):
    discos = Disco.objects.all()
    return render(request, 'listar_discos.html', {'discos': discos})


def cadastrar_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_discos')
    else:
        form = DiscoForm()
    return render(request, 'cadastrar_disco.html', {'form': form})


def editar_disco(request, disco_id):
    disco = Disco.objects.get(pk=disco_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('listar_discos')
    else:
        form = DiscoForm(instance=disco)
    return render(request, 'editar_disco.html', {'form': form, 'disco': disco})


def excluir_disco(request, disco_id):
    disco = Disco.objects.get(pk=disco_id)
    disco.delete()
    return redirect('listar_discos')
