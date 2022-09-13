from django.shortcuts import render
from recipes.models import Recipe
from ultis.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f"{recipes.first().category.name}"
    })


def recipe(request, id):
     return render(request, 'recipes/pages/recipe-views.html', context={
        'recipes': [make_recipe() for _ in range(1)],
        "list_details": True,
    })
