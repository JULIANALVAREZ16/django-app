from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("clientes/", views.list_clientes, name='clientes'),
    path("transacciones/", views.list_transacciones, name='transacciones'),
]