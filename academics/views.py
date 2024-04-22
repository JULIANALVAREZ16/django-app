from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def index(request):
    return HttpResponse("::welcome to my site::")

def list_users(request):
    #return HttpResponse("::Here you find list of people::")
    users = User.objects.all()
    return render(request, 'academics/list_users.html', {'users': users})

def create_users(request):
    return HttpResponse("::Here you find list of people::")