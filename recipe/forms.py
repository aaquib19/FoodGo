from django import forms
from .models import Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description','image')

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        # self.fields['location'].widget.attrs['placeholder'] = 'Type in your city.'
        # self.fields['address'].widget.attrs['placeholder'] = 'Type in your address.'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

