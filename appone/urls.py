from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('listar_pessoas', views.listar_pessoas, name="listar_pessoas"),
    path('criar_pessoa', views.criar_pessoa, name="criar_pessoa"),
]