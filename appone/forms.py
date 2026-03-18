from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "idade", "email", "telefone"]

        labels = {
            "nome": "Digite seu nome completo",
            "idade": "Digite sua idade",
            "email": "E-mail",
            "telefone": "Disque seu telefone"
        }

        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Digite seu nome"}),
            "idade": forms.TextInput(attrs={"placeholder": "Digite sua idade"}),
            "email": forms.TextInput(attrs={"placeholder": "Digite seu email"}),
            "telefone": forms.TextInput(attrs={"placeholder": "+55 83 9 8840-5666"}),
        }