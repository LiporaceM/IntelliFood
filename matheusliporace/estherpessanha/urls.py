from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    # path('saved_recipes/', views.saved_recipes, name='saved_recipes'),  # Descomentar quando implementar esta view
]
