import os
import random
from django.db import models
from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import  User

# Create your models here.
from FoodGo.utils import unique_slug_generator
from django.urls import reverse

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "recipe/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

class Recipe(models.Model):
    title           =       models.CharField(max_length=255)
    slug            =       models.SlugField(unique=True,blank=True,null=True)
    description     =       models.TextField()
    price           =       models.DecimalField(decimal_places=2,max_digits=10,default=100.00)
    image           =       models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    user            =       models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    #change filename so that we can avoid bad filename

    def get_absolute_url(self):
        # return '/recipe/{slug}'.format(slug=self.slug)
        return  reverse("recipe:detailView",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title #for python 2 :)


def recipe_pre_save_receiver(sender, instance ,*args ,**kwargs ):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(recipe_pre_save_receiver,sender=Recipe)