from django.db import models
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import  User
from django.db.models import Q
from recipe.models import Recipe
# Create your models here.
from FoodGo.utils import unique_slug_generator
from django.urls import reverse
# Create your models here.

class Ingredient(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    recipes  = models.ManyToManyField(Recipe,blank=True)

    def __str__(self):
        return self.title

    def save(self,*agrs,**kwargs):
        self.title = self.title.lower()
        return super(Ingredient, self).save(*agrs,**kwargs)


def ingredient_pre_save_receiver(sender, instance ,*args ,**kwargs ):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(ingredient_pre_save_receiver,sender=Ingredient)

