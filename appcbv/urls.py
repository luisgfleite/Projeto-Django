from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViaCepFormView.as_view(), name="form"),
]