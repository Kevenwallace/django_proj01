from django.urls import path

from recipes.views import home, my_view, contato


urlpatterns = [
    path('sobre/', my_view),
    path('contato/', contato),
    path('', home),
]
