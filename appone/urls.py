from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('listar/', views.listar_pessoas, name="listar_pessoas"),
    path('criar/', views.criar_pessoa, name="criar_pessoa"),
    path('editar/<int:pk>/', views.atualizar_pessoa, name="atualizar_pessoa"),
    path('apagar/<int:pk>/', views.apagar_pessoa, name="apagar_pessoa")
]