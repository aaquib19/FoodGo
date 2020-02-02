from django.urls import path

app_name = "search"
from .views import SearchRecipeView

urlpatterns = [
    path('', SearchRecipeView.as_view(), name="listView"),

]
