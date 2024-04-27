from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

from .models import Cliente, transaccione

def index(request):
    return HttpResponse("::welcome to my site::")

def list_clientes(request):
    #return HttpResponse("::welcome to clients")
    clientes = Cliente.objects.all()
    return render(request, 'finance/clientes.html', {'clientes': clientes})


def list_transacciones(request):
    transacciones = transaccione.objects.all()
    return render(request, 'finance/transacciones.html', {'transacciones': transacciones})
# Create your views here.
