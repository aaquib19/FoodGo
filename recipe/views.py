from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from django.http import HttpResponseForbidden

from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from  django.db import models
# Create your views here.

from .models import Recipe

class RecipeListView(ListView):
    queryset = Recipe.objects.all()
    paginate_by = 2
    template_name = 'recipe_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class RecipeDetailView(DetailView):
    queryset = Recipe.objects.all()
    template_name = 'recipe_detail.html'

    def get_object(self, *args,**kwargs):
        print("Fasdf")
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Recipe.objects.get(slug=slug)
        except Recipe.DoesNotExist:
            raise Http404("-------------   Recipe not found      --------------------")
        except Recipe.MultipleObjectsReturned:
            qs = Recipe.objects.filter(slug=slug)
            instance= qs.first()
        except:
            raise Http404("some error has occured check detail view")
        return  instance

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title','description','image']
    template_name = 'recipe_add.html'
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title','description','image']
    template_name="recipe_update.html"

    def dispatch(self, request, *args, **kwargs):
        '''Making sure that only authors can update the recipe'''
        obj = self.get_object()
        if obj.user != self.request.user:
            return HttpResponseForbidden()
        return super(RecipeUpdateView, self).dispatch(request,*args, **kwargs)

