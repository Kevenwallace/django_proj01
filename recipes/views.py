from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html')


def dale(request):
    return render(request, 'global/home.html')
