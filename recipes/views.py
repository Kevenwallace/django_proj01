from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_view(request):
    return HttpResponse("uma msg1")


def contato(request):
    return HttpResponse("contato")


def home(request):
    return HttpResponse("home")
