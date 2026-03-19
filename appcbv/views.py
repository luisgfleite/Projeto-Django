import requests
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import FormView, ListView, DeleteView, DetailView
from .models import ViaCep
from .forms import ViaCepForm

class ViaCepFormView(FormView):
    template_name = ""
    form_class = ViaCepForm
    success_url = reverse_lazy("viacep:list")

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "").strip()
        url = f'https://viacep.com.br/ws/{cep}/json/'
        req = requests.get(url)

        if req.status_code == 200:
            data = req.json()
            if "erro" not in data:
                cep_obj, created = ViaCep.objects.update_or_create(
                    cep = cep,
                    defaults={
                        "logradouro": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "localidade": data.get("localidade", ""),
                        "uf": data.get("uf", "") ,
                    },
                )

                self.object = cep_obj

                
            else:
                form.add_error("cep", "Cep não encontrado")
                return self.form_invalid(form)
        else:
            form.add_error("cep", "Api offline")
            return self.form_invalid(form)

        return super().form_valid(form)
    
