from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

DELETE_KEY = "KASDJLAKSDJLKASJDLASJDLKAJSKDJALKSJDKLAJ"

# Create your views here.
def home(request):
    return render(request, 'appone/home.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'appone/list.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    
    return render(request, 'appone/form.html', {'form': form})

def atualizar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect("listar_pessoas")
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'appone/update.html', {'form': form})

def apagar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    delete_key_get = request.GET.get("delete_key")
    form = PessoaForm(instance=pessoa)

    if delete_key_get is not None:
        if delete_key_get == DELETE_KEY:
            pessoa.delete()
            return redirect('listar_pessoas')
    else:
        return render(request, 'appone/confirm_page.html', {'pessoa': pessoa})