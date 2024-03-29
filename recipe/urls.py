from django.urls import path

from .views import RecipeListView, RecipeDetailView, RecipeUpdateView, RecipeCreateView

app_name = "recipe"

urlpatterns = [
    path('', RecipeListView.as_view(), name="listView"),
    path('add/', RecipeCreateView.as_view(), name="createView"),

    path('<slug:slug>/', RecipeDetailView.as_view(), name="detailView"),
    path('<slug:slug>/edit', RecipeUpdateView.as_view(), name="editView"),

]
