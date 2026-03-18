from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

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