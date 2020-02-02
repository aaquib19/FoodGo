from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from recipe.models import Recipe


# Create your views here.
class SearchRecipeView(ListView):
    queryset = Recipe.objects.all()
    paginate_by = 6
    template_name = 'search_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchRecipeView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Recipe.objects.search(query)
        return Recipe.objects.all()
