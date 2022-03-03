from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ToDo/index.html')


def login(request):
    return render(request, 'ToDo/login.html')


def register(request):
    return render(request, 'ToDo/register.html')


def home(request):
    return render(request, 'ToDo/home.html')