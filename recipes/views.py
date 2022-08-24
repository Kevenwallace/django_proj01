from django.shortcuts import render

from ultis.recipes.factory import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipes': [make_recipe() for _ in range(1)],
        "list_details": True,
    })
