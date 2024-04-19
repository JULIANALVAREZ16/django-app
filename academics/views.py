from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("::welcome to my site::")

def list_persons(request):
    return HttpResponse("::Here you find list of people::")